from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from web.models import Note, Tag


def main_view(request):
    return redirect("notes_list")


def notes_view(request):
    notes = Note.objects.all()

    with_alerts = 'with_alerts' in request.GET
    if with_alerts:
        notes = notes.filter(alert_send_at__isnull=False)
    search = request.GET.get("search", None)

    if search:
        # title__contains="..." SELECT * FROM web_note WHERE title LIKE = "%...%"
        # title__icontains="..." SELECT * FROM web_note WHERE UPPER(title) LIKE = UPPER("%...%")
        notes = notes.filter(
            Q(title__icontains=search) |
            Q(text__icontains=search)
        )
    try:
        tag_id = int(request.GET.get("tag_id", None))
    except (ValueError, TypeError):
        tag_id = None
    if tag_id:
        tag = Tag.objects.get(id=tag_id)
        notes = notes.filter(tags__in=[tag])

    return render(request, "web/main.html", {
        'count': Note.objects.count(),
        'notes': notes,
        'with_alerts': with_alerts,
        'query_params': request.GET,
        'search': search,
        'tags': Tag.objects.all(),
        'tag_id': tag_id
    })


def note_view(request, id):
    note = Note.objects.get(id=id)
    return render(request, "web/note.html", {
        'note': note
    })
