def find_notes(notes, query):
    query = query.strip().lower()
    if not query:
        return []
    return [note for note in notes if query in note.lower()]
