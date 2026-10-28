import json
from pathlib import Path

from search import find_notes

notes = json.loads(Path(__file__).with_name("notes.json").read_text(encoding="utf-8"))

for query in ("git", "GIT", "  git  "):
    print(f"{query!r} -> {find_notes(notes, query)!r}")
