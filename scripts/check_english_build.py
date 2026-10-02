"""Check rendered English text, including fallback labels absent from source i18n."""
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
from urllib.parse import urlsplit

from check_english_content import HAN, ROOT

VOID_TAGS = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
             'link', 'meta', 'param', 'source', 'track', 'wbr'}
TEXT_ATTRIBUTES = {'alt', 'title', 'aria-label', 'aria-description', 'placeholder'}
SEARCH_INDEXES = (
    'search-index-default.json',
    'search-index-docs-default-current.json',
    'search-index-docs-sdk-current.json',
    'search-index-docs-server-current.json',
    'search-index-docs-tokenbank-current.json',
)


class EnglishPage(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
        self.language = None

    def reject_chinese(self, value, location):
        if HAN.search(value):
            self.errors.append(f'{location}: Chinese text in rendered English page: {value[:120]!r}')

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == 'html':
            self.language = attributes.get('lang')
        for key, value in attrs:
            if value and (key in TEXT_ATTRIBUTES or (tag == 'meta' and key == 'content')):
                self.reject_chinese(value, f'<{tag}> {key}')
        if tag not in VOID_TAGS:
            self.stack.append((tag, attributes))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID_TAGS:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break

    def is_language_switch(self, value):
        # Only the native-language name in Docusaurus's locale switch is allowed.
        # A lang attribute on article content must not hide untranslated prose.
        if value != '简体中文':
            return False
        for tag, attrs in reversed(self.stack):
            if tag != 'a':
                continue
            href = attrs.get('href') or ''
            target = urlsplit(href)
            return (attrs.get('lang') == 'zh-CN'
                    and 'dropdown__link' in (attrs.get('class') or '').split()
                    and href.startswith('/') and not target.scheme and not target.netloc
                    and 'en' not in target.path.split('/'))
        return False

    def handle_data(self, data):
        if any(tag in {'script', 'style'} for tag, _ in self.stack):
            return
        value = data.strip()
        if value and not self.is_language_switch(value):
            self.reject_chinese(value, ' > '.join(tag for tag, _ in self.stack))


def audit_html(body):
    page = EnglishPage()
    page.feed(body)
    page.close()
    if page.language != 'en-US':
        page.errors.append(f'Expected html lang=en-US, found {page.language!r}')
    return page.errors


def json_has_chinese(value):
    if isinstance(value, str):
        return bool(HAN.search(value))
    if isinstance(value, list):
        return any(json_has_chinese(item) for item in value)
    if isinstance(value, dict):
        return any(json_has_chinese(key) or json_has_chinese(item)
                   for key, item in value.items())
    return False


def audit_build(english_root):
    errors = []
    # Do not allow a missing or partial build to pass a vacuous text scan.
    for name in ('index', '404', 'sdk', 'server', 'openwrt', 'tokenbank'):
        if not (english_root / f'{name}.html').is_file() and not (english_root / name / 'index.html').is_file():
            errors.append(f'{name}: required English page missing; build both locales first')
    for path in sorted(english_root.rglob('*.html')):
        try:
            errors.extend(f'{path.relative_to(english_root).as_posix()}: {error}'
                          for error in audit_html(path.read_text(encoding='utf-8')))
        except (UnicodeError, ValueError) as error:
            errors.append(f'{path.name}: invalid English HTML: {error}')
    for name in SEARCH_INDEXES:
        if not (english_root / name).is_file():
            errors.append(f'{name}: English search index missing')
    for path in sorted(english_root.glob('search-index-*.json')):
        try:
            if json_has_chinese(json.loads(path.read_text(encoding='utf-8'))):
                errors.append(f'{path.name}: Chinese text in English search index')
        except (UnicodeError, ValueError):
            errors.append(f'{path.name}: invalid English search JSON')
    return errors


def main():
    english_root = ROOT / 'build/en'
    errors = audit_build(english_root)
    if errors:
        # ASCII escaping keeps CI diagnostics readable on legacy Windows consoles.
        print('\n'.join(error.encode('ascii', 'backslashreplace').decode('ascii')
                        for error in errors), file=sys.stderr)
        return 1
    print(f'English build OK: {len(list(english_root.rglob("*.html")))} HTML pages '
          '(navigation, breadcrumbs, content, accessible labels and metadata) and search indexes checked.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
