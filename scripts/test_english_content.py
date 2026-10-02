"""Language regression tests use isolated fixtures, never edit repository docs."""
import json
from pathlib import Path
import tempfile
import unittest

from check_english_content import audit, TREES, PAIRS


class EnglishContentTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        for tree in TREES:
            self.put(f'i18n/en/{tree}/current/intro.md', '# Introduction\n')
        for relative in PAIRS:
            path = Path(relative)
            translation = path.with_name(path.stem + '_zh.md')
            self.put(relative, f'# Guide\n\n[Chinese]({translation.name})\n')
            self.put(str(translation), f'# 中文说明\n\n[English]({path.name})\n')

    def put(self, relative, body):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding='utf-8')

    def test_separate_chinese_files_are_allowed(self):
        self.put('README_zh.md', '# 中文入口')
        self.put('docs-server/intro.md', '# 中文站点')
        self.assertEqual(audit(self.root), [])

    def test_root_readme_and_media_chinese_rejected_with_line(self):
        self.put('README.md', '# Example\n\n中文混入\n')
        self.put('docs/media/new-guide.md', '# Capture\n中文说明')
        errors = audit(self.root)
        self.assertTrue(any('README.md:3:' in item for item in errors))
        self.assertTrue(any('new-guide.md:2:' in item for item in errors))

    def test_english_mdx_and_code_examples_are_checked(self):
        self.put(f'i18n/en/{TREES[0]}/current/example.mdx', '# Example\n```python\n# 中文注释\n```')
        self.assertTrue(any('example.mdx:3:' in item for item in audit(self.root)))

    def test_chinese_translation_keys_allowed_but_messages_rejected(self):
        path = f'i18n/en/{TREES[0]}/current.json'
        self.put(path, json.dumps({'sidebar.快速入门': {'message': 'Quickstart'}}))
        self.assertEqual(audit(self.root), [])
        self.put(path, json.dumps({'sidebar.快速入门': {'message': 'Quickstart 快速入门'}}))
        self.assertTrue(any('translation message' in item for item in audit(self.root)))

    def test_missing_pairs_and_links_fail(self):
        (self.root / 'LICENSING_zh.md').unlink()
        self.put('CONTRIBUTING.md', '# Guide\n')
        errors = audit(self.root)
        self.assertTrue(any('missing language pair' in item for item in errors))
        self.assertTrue(any('missing reciprocal language link' in item for item in errors))

    def test_missing_documentation_tree_cannot_pass(self):
        (self.root / f'i18n/en/{TREES[0]}/current/intro.md').unlink()
        self.assertTrue(any('missing or empty' in item for item in audit(self.root)))


if __name__ == '__main__':
    unittest.main()
