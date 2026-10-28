# Developer Notes Search

A tiny course project that searches fictional note titles. Python 3 and its standard library are sufficient; no packages, database or web server are required.

`search.py` contains find_notes. `notes.json` contains sample titles. `demo.py` prints three example calls. `check_search.py` contains a few explicit acceptance examples.

From this folder, run `python3 demo.py` and `python3 check_search.py`. On Windows with the Python launcher, use `py -3 demo.py` and `py -3 check_search.py`.

This is the starter state. Matching is case-insensitive, but surrounding whitespace is not yet ignored. The padded-query check is intentionally expected to fail until the planned change is implemented; the other six cases should pass. That is the real behavior under investigation, not a staged AI mistake.

Task: ignore surrounding whitespace in the query while preserving case-insensitive substring matching, original note order, and empty/whitespace-only queries returning an empty list. Change only search.py. The sample data, caller and supplied checks should remain unchanged.
