"""Exercise generated-page leaks that Markdown-only checks cannot detect."""
import json
from pathlib import Path
import tempfile
import unittest

from check_english_build import audit_build, audit_html, SEARCH_INDEXES


def page(content):
    return f'<!doctype html><html lang="en-US"><body>{content}</body></html>'


class EnglishPageTests(unittest.TestCase):
    def test_english_navigation_and_breadcrumbs(self):
        self.assertEqual(audit_html(page('<nav>Agent design and development</nav>'
                                        '<ol><li>Detailed API reference</li></ol>')), [])

    def test_both_missing_translation_fallbacks_are_rejected(self):
        errors = audit_html(page('<nav hidden><button>Agent 设计与开发</button></nav>'
                                 '<ol aria-label="Breadcrumbs"><li>完整接口参考</li></ol>'))
        self.assertEqual(len(errors), 2)
        self.assertIn('Agent 设计与开发', errors[0])
        self.assertIn('完整接口参考', errors[1])

    def test_real_language_selector_is_allowed_for_root_and_pages_base(self):
        for base in ('/', '/nexus-docs/'):
            with self.subTest(base=base):
                content = f'<a class="dropdown__link" lang="zh-CN" href="{base}sdk/intro">简体中文</a>'
                self.assertEqual(audit_html(page(content)), [])

    def test_chinese_outside_language_selector_is_not_exempt(self):
        for content in ('<p>简体中文</p>', '<section lang="zh-CN">中文内容</section>',
                        '<a lang="zh-CN" href="/sdk">简体中文</a>',
                        '<a class="dropdown__link" lang="zh-CN" href="/en/sdk">简体中文</a>',
                        '<a class="dropdown__link" lang="zh-CN" href="//other.example/sdk">简体中文</a>',
                        '<a class="dropdown__link" lang="zh-CN" href="/sdk">中文正文</a>'):
            with self.subTest(content=content):
                self.assertTrue(audit_html(page(content)))

    def test_titles_accessible_text_and_metadata(self):
        for content in ('<title>中文标题</title>', '<img alt="示例" src="image.svg">',
                        '<input placeholder="搜索">', '<button aria-label="下一页"></button>',
                        '<span title="中文说明"></span>', '<meta name="description" content="中文介绍">'):
            with self.subTest(content=content):
                self.assertTrue(audit_html(page(content)))

    def test_entity_encoded_text_is_checked(self):
        self.assertTrue(audit_html(page('<p>&#20013;&#25991;</p>')))

    def test_script_keys_and_comments_are_not_user_facing(self):
        self.assertEqual(audit_html(page('<script>{"中文键": "English"}</script>'
                                        '<style>/* 中文 */</style><!-- 中文 -->')), [])

    def test_void_elements_do_not_extend_language_exemption(self):
        self.assertTrue(audit_html(page('<a class="dropdown__link" lang="zh-CN" href="/sdk">'
                                       '<img src="flag.svg">简体中文</a><br><p>简体中文</p>')))

    def test_english_document_language_is_required(self):
        self.assertTrue(audit_html('<html lang="zh-CN">English</html>'))
        self.assertTrue(audit_html('<p>English</p>'))


class EnglishBuildTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        for name in ('index', '404', 'sdk', 'server', 'openwrt', 'tokenbank'):
            self.put(f'{name}.html', page('<h1>English</h1>'))
        for name in SEARCH_INDEXES:
            self.put(name, json.dumps([{'title': 'Introduction', 'content': 'English content'}]))

    def put(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')

    def test_clean_build_passes(self):
        self.assertEqual(audit_build(self.root), [])

    def test_all_nested_pages_are_checked(self):
        self.put('sdk/reference/modules/browser.html', page('<nav>完整接口参考</nav>'))
        errors = audit_build(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn('sdk/reference/modules/browser.html', errors[0])

    def test_missing_or_partial_build_fails(self):
        self.assertTrue(audit_build(self.root / 'missing'))
        (self.root / 'sdk.html').unlink()
        self.assertTrue(any('required English page missing' in item for item in audit_build(self.root)))

    def test_search_index_checks_decoded_values_and_keys(self):
        for value in ([{'title': '中文结果'}], {'中文': 'English'}):
            with self.subTest(value=value):
                self.put(SEARCH_INDEXES[0], json.dumps(value, ensure_ascii=True))
                self.assertTrue(any('Chinese text in English search index' in item for item in audit_build(self.root)))

    def test_missing_and_invalid_search_index_fail(self):
        (self.root / SEARCH_INDEXES[0]).unlink()
        self.put(SEARCH_INDEXES[1], '{bad json')
        errors = audit_build(self.root)
        self.assertTrue(any('search index missing' in item for item in errors))
        self.assertTrue(any('invalid English search JSON' in item for item in errors))


if __name__ == '__main__':
    unittest.main()
