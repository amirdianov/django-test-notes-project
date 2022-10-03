from django import forms
from django.core.exceptions import ValidationError


class NoteForm(forms.Form):
    title = forms.CharField(label='Название')
    text = forms.CharField(widget=forms.Textarea(), label='Текст')
