from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(BaseModel):
    title = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_tag = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True
    )


class Note(BaseModel):
    title = models.CharField(max_length=500)
    text = models.TextField()
    alert_send_at = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'Note {self.id} "{self.title}"'