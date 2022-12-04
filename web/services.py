from web.models import Note


def share_note(note: Note):
    note.is_shared = True
    note.save()