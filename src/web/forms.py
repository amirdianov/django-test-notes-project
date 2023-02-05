from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse

from web.models import Note, NoteComment
from web.tasks import send_comment_notification


class NoteForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        self.instance.user = self.initial["user"]
        return super(NoteForm, self).save(*args, **kwargs)

    class Meta:
        model = Note
        fields = ("title", "text", "file", "image")


class AuthForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


class NoteCommentForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        self.instance.user = self.initial["user"]
        note = self.initial["note"]
        self.instance.note = note
        instance = super(NoteCommentForm, self).save(*args, **kwargs)
        request = self.initial["request"]
        link = request.build_absolute_uri(reverse("note", args=(note.title, note.id)))
        send_comment_notification.delay(instance.id, link)
        return instance

    class Meta:
        model = NoteComment
        fields = ("text",)
