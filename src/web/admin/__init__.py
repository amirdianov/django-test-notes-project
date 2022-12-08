from django.contrib import admin, messages

# Register your models here.
from web.admin.note import NoteAdmin
from web.admin.tag import TagAdmin
from web.models import Note, Tag, NoteComment, User
from web.admin.user import UserAdmin

admin.site.register(Note, NoteAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(User, UserAdmin)
