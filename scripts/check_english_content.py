"""Reject Chinese prose in English docs, without flagging i18n lookup keys."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
HAN = re.compile(r'[\u3007\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U000323af]')
TREES = ('docusaurus-plugin-content-docs', 'docusaurus-plugin-content-docs-sdk',
         'docusaurus-plugin-content-docs-server', 'docusaurus-plugin-content-docs-tokenbank')
PAIRS = ('CONTRIBUTING.md', 'LICENSING.md', 'docs/media/capture-notes.md')


def chinese_variant(path):
    return path.stem.endswith(('_zh', '.zh', '.zh-CN', '.zh-Hans'))


def english_files(root):
    paths = set(root.glob('*.md')) | set(root.glob('*.mdx'))
    for tree in (root / 'i18n/en', root / 'docs'):
        paths.update(tree.rglob('*.md'))
        paths.update(tree.rglob('*.mdx'))
    return sorted(path for path in paths if not chinese_variant(path))


def audit(root):
    errors = []
    for tree in TREES:
        directory = root / 'i18n/en' / tree / 'current'
        if not any(directory.rglob('*.md')):
            errors.append(f'{directory.relative_to(root)}: English documentation tree is missing or empty')
    for path in english_files(root):
        for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            if HAN.search(line):
                errors.append(f'{path.relative_to(root).as_posix()}:{number}: Chinese text in English Markdown; move it to a Chinese document')
    # Docusaurus keys may be Chinese, but the visible English message must not be.
    import json
    for path in sorted((root / 'i18n/en').rglob('*.json')):
        try:
            entries = json.loads(path.read_text(encoding='utf-8'))
            if not isinstance(entries, dict):
                raise ValueError('Expected translation object')
            for key, value in entries.items():
                if isinstance(value, dict) and isinstance(value.get('message'), str) and HAN.search(value['message']):
                    errors.append(f'{path.relative_to(root).as_posix()}: {key}: Chinese text in English translation message')
        except (ValueError, UnicodeError):
            errors.append(f'{path.relative_to(root).as_posix()}: invalid translation JSON')
    for relative in PAIRS:
        source = root / relative
        translation = source.with_name(source.stem + '_zh.md')
        for path, other in ((source, translation), (translation, source)):
            if not path.is_file():
                errors.append(f'{path.relative_to(root).as_posix()}: missing language pair')
            elif f']({other.name})' not in path.read_text(encoding='utf-8'):
                errors.append(f'{path.relative_to(root).as_posix()}: missing reciprocal language link')
    return errors


def main():
    errors = audit(ROOT)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'English content OK: {len(english_files(ROOT))} Markdown files; visible i18n messages and language links checked.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
