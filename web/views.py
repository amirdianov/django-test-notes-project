from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from web.models import Note, Tag


def main_view(request):
    return render(request, "web\main.html")