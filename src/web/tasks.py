from notes.celery import app
from web.models import NoteComment


@app.task
def send_comment_notification(note_comment_id: int):
    note_comment = NoteComment.objects.get(id=note_comment_id)
    note = note_comment.note
    print(f"Уведомление отправлено автору {note.user} заметки {note}")
