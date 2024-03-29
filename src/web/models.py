import os

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.db.models import QuerySet, Count, CheckConstraint, Q, UniqueConstraint, Prefetch
from django.utils.datetime_safe import datetime
from stdimage import StdImageField

from web.enums import Role


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(DjangoUserManager):
    def _create_user(self, email, password, commit=True, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, role=Role.admin, **extra_fields)


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField(unique=True)
    role = models.CharField(choices=Role.choices, max_length=15, default=Role.user)
    name = models.CharField(max_length=255, null=True, blank=True)

    @property
    def is_staff(self):
        return self.role in (Role.admin, Role.staff)

    @property
    def is_superuser(self):
        return self.role == Role.admin

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"


class Tag(BaseModel):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_tag = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "тег"

        verbose_name_plural = "теги"

    def __str__(self):
        return f"{self.title}"


class NoteQuerySet(QuerySet):
    def optimize_for_lists(self):
        last_comments = NoteComment.objects.all().order_by("note_id", "-created_at").distinct("note_id")
        return (
            self.select_related("user")
            .prefetch_related(Prefetch("comments", last_comments, to_attr="last_comments"))
            .annotate(comments_count=Count("comments"))
        )

    def has_access(self, user=None):
        clause = Q(is_shared=True)
        if user:
            clause |= Q(user=user)
        return self.filter(clause)


def get_note_file_path(instance, filename):
    return os.path.join("note_files", instance.created_at.strftime("%Y-%m-%d"), filename)


def get_note_image_path(instance, filename):
    return os.path.join("note_images", instance.created_at.strftime("%Y-%m-%d"), filename)


class Note(BaseModel):
    objects = NoteQuerySet.as_manager()

    title = models.CharField(max_length=500, verbose_name="Название", help_text="Название заметки")
    text = models.TextField(verbose_name="Текст")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    alert_send_at = models.DateTimeField(null=True, blank=True, verbose_name="Время напоминания")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Теги")
    file = models.FileField(
        upload_to=get_note_file_path,
        null=True,
        blank=True,
        verbose_name="Файл",
    )
    image = StdImageField(
        upload_to=get_note_image_path,
        null=True,
        blank=True,
        verbose_name="Картинка",
        variations={
            "thumbnail": {
                "height": 400,
                "width": 400,
            }
        },
    )
    is_shared = models.BooleanField(default=False)

    class Meta:
        verbose_name = "заметка"
        verbose_name_plural = "заметки"
        ordering = ("created_at",)

        constraints = [
            CheckConstraint(
                name="alert_send_at_after",
                check=(
                    Q(alert_send_at__gte=datetime(2022, 1, 1), alert_send_at__isnull=False)
                    | Q(alert_send_at__isnull=True)
                ),
            ),
            UniqueConstraint(name="unique_content", fields=("title", "text")),
        ]

    def __str__(self):
        return f'Note {self.id} "{self.title}"'


class NoteComment(BaseModel):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, verbose_name="Заметка", related_name="comments")
    text = models.TextField(verbose_name="Текст")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор комментария", null=True, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"
