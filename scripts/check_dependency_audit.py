"""Keep reviewed build risks visible; fail closed on drift or failed guards."""
import json
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent.parent
REVIEWED = {
    "https://github.com/advisories/GHSA-w3rx-r6r6-pgpr": ("image-size", "2.0.2"),
    "https://github.com/advisories/GHSA-5p2g-fcmc-qvqq": ("image-size", "2.0.2"),
    "https://github.com/advisories/GHSA-vfj7-8cjw-p6xm": ("braces", "3.0.3"),
    "https://github.com/advisories/GHSA-ch52-4w7c-c8xp": ("http-cache-semantics", "4.2.0"),
}


def review_findings(data, lock):
    errors = []
    for name, item in data["vulnerabilities"].items():
        if item.get("severity") == "critical":
            errors.append(name)
        for via in item.get("via", []):
            if not isinstance(via, dict):
                continue  # npm transitive effects; inspect their root advisories.
            rule = REVIEWED.get(via.get("url"))
            if not rule or rule[0] != name or not item.get("nodes"):
                errors.append(via.get("url", name))
                continue
            for node in item["nodes"]:
                if lock["packages"].get(node, {}).get("version") != rule[1]:
                    errors.append(f"Review changed dependency: {name}")
    return errors


def main():
    npm = "npm.cmd" if os.name == "nt" else "npm"
    result = subprocess.run([npm, "audit", "--json"], cwd=ROOT,
                            capture_output=True, text=True, timeout=180)
    try:
        data = json.loads(result.stdout)
    except ValueError:
        raise SystemExit("Dependency audit unavailable; review failed.") from None
    if result.returncode not in (0, 1) or data.get("error") or "vulnerabilities" not in data:
        raise SystemExit("Dependency audit unavailable; review failed.")
    errors = review_findings(data, json.loads((ROOT / "package-lock.json").read_text()))
    print(json.dumps(data["metadata"]["vulnerabilities"]), flush=True)
    if errors:
        raise SystemExit("Dependency advisory requires review: " + ", ".join(sorted(set(errors))))
    # Standalone audit must verify containment too, not merely accept GHSA IDs.
    guard_tests = subprocess.run([npm, "run", "check:security"], cwd=ROOT, timeout=180)
    if guard_tests.returncode:
        raise SystemExit("Dependency containment verification failed; publication blocked.")
    if data["vulnerabilities"]:
        print("KNOWN UPSTREAM RISKS REMAIN: image-size, braces and http-cache-semantics. "
              "Docs build containment verified; see SECURITY.md. Not an upstream patch.")


if __name__ == "__main__":
    main()
