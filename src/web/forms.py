from django import forms
from django.core.exceptions import ValidationError

from web.models import Note


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
