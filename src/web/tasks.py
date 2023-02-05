from django.conf import settings
from django.core.mail import send_mail

from notes.celery import app
from web.models import NoteComment


@app.task
def send_comment_notification(note_comment_id: int):
    note_comment = NoteComment.objects.get(id=note_comment_id)
    note = note_comment.note

    text = f"К заметке {note.title} был оставлен комментарий: \n{note_comment.text}"

    send_mail(
        "Новый комментарий",
        text,
        settings.DEFAULT_FROM_EMAIL,
        [note.user.email],
    )
