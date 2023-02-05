from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from notes.celery import app
from web.models import NoteComment


@app.task
def send_comment_notification(note_comment_id: int, link: str):
    note_comment = NoteComment.objects.get(id=note_comment_id)
    note = note_comment.note

    rendered = render_to_string(
        "web/emails/comment_notification.html",
        {
            "user_name": note.user.name,
            "link": link,
            "note_title": note.title,
            "comment_text": note_comment.text,
        },
    )

    send_mail("Новый комментарий", "", settings.DEFAULT_FROM_EMAIL, [note.user.email], html_message=rendered)
