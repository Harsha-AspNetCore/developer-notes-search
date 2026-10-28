import argparse
import json
from pathlib import Path

from search import find_notes

parser = argparse.ArgumentParser(description="Search developer note titles.")
parser.add_argument("query", help="text to look for in note titles")
args = parser.parse_args()

notes = json.loads(Path(__file__).with_name("notes.json").read_text(encoding="utf-8"))
matches = find_notes(notes, args.query)

if matches:
    for title in matches:
        print(title)
else:
    print("No matching notes.")
