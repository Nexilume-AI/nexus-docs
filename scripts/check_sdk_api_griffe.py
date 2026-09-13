"""Verify bilingual API coverage from the SDK's static Griffe model."""

from pathlib import Path
import os
import sys

from griffe import load


SITE_ROOT = Path(__file__).resolve().parents[1]
SDK_SOURCE = Path(os.environ.get("NEXUS_SDK_SOURCE", "sdk-source/src"))
REFERENCE_PAGES = (
    SITE_ROOT / "docs-sdk/reference/api.md",
    SITE_ROOT / "i18n/en/docusaurus-plugin-content-docs-sdk/current/reference/api.md",
)


def main() -> int:
    package = load("nexus_agent", search_paths=[SDK_SOURCE])
    if package.exports is None:
        print("nexus_agent.__all__ was not found", file=sys.stderr)
        return 1
    names = sorted(str(name) for name in package.exports)
    failed = False
    for page in REFERENCE_PAGES:
        content = page.read_text(encoding="utf-8")
        missing = [name for name in names if f"`{name}`" not in content]
        if missing:
            failed = True
            print(f"{page}: missing {', '.join(missing)}", file=sys.stderr)
    if failed:
        return 1
    print(f"Griffe API coverage OK: {len(names)} exports documented in both locales.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
