from django.http import HttpResponse
from django.shortcuts import render

from web.models import Note, Tag


def main_view(request):
    notes = Note.objects.all()
    with_alerts = 'with_alerts' in request.GET
    if with_alerts:
        notes = notes.filter(alert_send_at__isnull=False)

    return render(request, "web/main.html", {
            'count': Note.objects.count(),
            'notes': notes,
            'with_alerts': with_alerts,
            'query_params': request.GET
        })