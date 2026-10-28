import json
from pathlib import Path

from search import find_notes

notes = json.loads(Path(__file__).with_name("notes.json").read_text(encoding="utf-8"))
cases = [
    ("plain", "git", ["Git basics"]),
    ("uppercase", "GIT", ["Git basics"]),
    ("padded", "  git  ", ["Git basics"]),
    ("other-title", "python", ["Python tips"]),
    ("empty", "", []),
    ("spaces-only", "   ", []),
    ("no-match", "missing-note", []),
]

passed = 0
for name, query, expected in cases:
    actual = find_notes(notes, query)
    if actual == expected:
        passed += 1
        print(f"PASS {name}")
    else:
        print(f"FAIL {name}: expected {expected!r}, got {actual!r}")

print(f"{passed}/{len(cases)} checks passed")
raise SystemExit(0 if passed == len(cases) else 1)
