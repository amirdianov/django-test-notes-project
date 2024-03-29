from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count, Max, Min
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, RedirectView, FormView, CreateView, UpdateView, DeleteView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from web.forms import NoteForm, AuthForm, NoteCommentForm
from web.models import Note, Tag, User
from web.services import share_note


class NotesListView(ListView):
    template_name = "web/main.html"

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Note.objects.none()
        queryset = Note.objects.filter(user=self.request.user).optimize_for_lists().order_by("-created_at")
        return self.filter_queryset(queryset)

    def filter_queryset(self, notes):
        self.with_alerts = "with_alerts" in self.request.GET
        self.search = self.request.GET.get("search", None)
        try:
            self.tag_id = int(self.request.GET.get("tag_id", None))
        except (TypeError, ValueError):
            self.tag_id = None

        if self.with_alerts:
            notes = notes.filter(alert_send_at__isnull=False)

        if self.search:
            # title="..." SELECT * FROM web_note WHERE title = "..."
            # title__iexact="..." SELECT * FROM web_note WHERE UPPER(title) = UPPER("...")
            # title__contains="..." SELECT * FROM web_note WHERE title LIKE = "%...%"
            # title__icontains="..." SELECT * FROM web_note WHERE UPPER(title) LIKE = UPPER("%...%")
            notes = notes.filter(Q(title__icontains=self.search) | Q(text__icontains=self.search))

        if self.tag_id:
            tag = Tag.objects.get(id=self.tag_id)
            notes = notes.filter(tags__in=[tag])
        return notes

    def get_context_data(self, *, object_list=None, **kwargs):
        if not self.request.user.is_authenticated:
            return {}
        return {
            **super(NotesListView, self).get_context_data(),
            "count": Note.objects.filter(user=self.request.user).count(),
            "with_alerts": self.with_alerts,
            "search": self.search,
            "tag_id": self.tag_id,
            "query_params": self.request.GET,
            "tags": Tag.objects.filter(user=self.request.user),
        }


class NoteDetailView(DetailView):
    template_name = "web/note.html"
    slug_field = "id"
    slug_url_kwarg = "id"

    def get_queryset(self):
        user = None if self.request.user.is_anonymous else self.request.user
        return Note.objects.all().has_access(user)

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "comment_form": NoteCommentForm(initial={"note_id": self.object.id}),
        }


def note_comment(request, id):
    user = None if request.user.is_anonymous else request.user
    note = Note.objects.all().has_access(user).filter(id=id).first()
    if not note:
        raise Http404
    form = NoteCommentForm(data=request.POST, initial={"user": user, "note": note, "request": request})
    if not form.is_valid():
        return HttpResponse("Ошибка при создании комментария, попробуйте еще раз")
    form.save()
    return redirect("note", note.title, note.id)


class NoteMixin:
    template_name = "web/note_form.html"
    slug_field = "id"
    slug_url_kwarg = "id"

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Note.objects.none()
        return Note.objects.filter(user=self.request.user)

    def get_initial(self):
        return {"user": self.request.user}

    def get_success_url(self):
        return reverse("note", args=(self.object.title, self.object.id))


class NoteCreateFormView(NoteMixin, CreateView):
    form_class = NoteForm


class NoteUpdateView(NoteMixin, UpdateView):
    form_class = NoteForm

    def get_context_data(self, **kwargs):
        return {
            **super(NoteUpdateView, self).get_context_data(**kwargs),
            "id": self.kwargs[self.slug_url_kwarg],
            "title": self.object.title,
        }


class NoteDeleteView(NoteMixin, DeleteView):
    template_name = "web/note_delete.html"

    def get_success_url(self):
        return reverse("main")


class RegistrationView(View):
    def _render(self, request, form=None, is_success=False):
        return render(request, "web/registration.html", {"form": form or AuthForm(), "is_success": is_success})

    def get(self, request, *args, **kwargs):
        return self._render(request)

    def post(self, request, *args, **kwargs):
        is_success = False
        form = AuthForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            is_success = True
        return self._render(request, form, is_success)


def login_view(request):
    form = AuthForm()
    message = None
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is None:
                message = "Электронная почта или пароль неправильные"
            else:
                login(request, user)
                next_url = "main"
                if "next" in request.GET:
                    next_url = request.GET.get("next")
                return redirect(next_url)
    return render(request, "web/login.html", {"form": form, "message": message})


def logout_view(request):
    logout(request)
    return redirect("main")


def html_view(request):
    return render(request, "web/html.html")


@login_required
def stat_view(request):
    notes = Note.objects.filter(user=request.user)
    return render(
        request,
        "web/stat.html",
        notes.aggregate(
            count=Count("id"),
            count_with_alerts=Count("id", filter=Q(alert_send_at__isnull=False)),
            last_created_at=Max("created_at"),
            first_created_at=Min("created_at"),
            last_updated_at=Max("created_at"),
        ),
    )


@csrf_exempt
def example_api_view(request):
    return JsonResponse({"status": "ok"})


@api_view(["GET", "POST", "PUT"])
def example_api2_view(request):
    """Тестовое API"""
    return Response({"status": "ok"})


@login_required
def note_share(request, title, id):
    note = get_object_or_404(Note, id=id)
    share_note(note)
    return redirect("note", title, id)
