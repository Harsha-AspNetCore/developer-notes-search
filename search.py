def find_notes(notes, query):
    if not query:
        return []
    query = query.lower()
    return [note for note in notes if query in note.lower()]
