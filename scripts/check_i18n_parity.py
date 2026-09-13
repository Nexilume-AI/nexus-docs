"""Ensure Chinese and English documentation trees contain matching Markdown pages."""

from pathlib import Path
import sys


SITE_ROOT = Path(__file__).resolve().parents[1]
PAIRS = (
    (
        SITE_ROOT / "docs-server",
        SITE_ROOT / "i18n/en/docusaurus-plugin-content-docs-server/current",
        "Server current",
    ),
    (
        SITE_ROOT / "docs-tokenbank",
        SITE_ROOT / "i18n/en/docusaurus-plugin-content-docs-tokenbank/current",
        "TokenBank current",
    ),
    (
        SITE_ROOT / "docs-openwrt",
        SITE_ROOT / "i18n/en/docusaurus-plugin-content-docs/current",
        "OpenWrt current",
    ),
    (
        SITE_ROOT / "docs-sdk",
        SITE_ROOT / "i18n/en/docusaurus-plugin-content-docs-sdk/current",
        "SDK current",
    ),
)


def markdown_paths(root: Path) -> set[Path]:
    return {path.relative_to(root) for path in root.rglob("*.md")}


def main() -> int:
    failed = False
    total = 0
    for source, translation, label in PAIRS:
        source_paths = markdown_paths(source)
        translation_paths = markdown_paths(translation)
        total += len(source_paths)
        missing = sorted(source_paths - translation_paths)
        extra = sorted(translation_paths - source_paths)
        if missing or extra:
            failed = True
            if missing:
                print(f"{label}: missing English: {', '.join(map(str, missing))}", file=sys.stderr)
            if extra:
                print(f"{label}: English-only: {', '.join(map(str, extra))}", file=sys.stderr)
        else:
            print(f"{label}: {len(source_paths)} Markdown pages match")
    if failed:
        return 1
    print(f"i18n parity OK: {total} Chinese pages have matching English pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
