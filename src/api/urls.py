"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import SimpleRouter

from api.views import status_view, NoteViewSet, auth_view, profile_view, TagsViewSet

router = SimpleRouter()
router.register("notes", NoteViewSet, basename="notes")
router.register("tags", TagsViewSet, basename="tags")

schema_view = get_schema_view(
    openapi.Info(
        title="Notes API",
        default_version="v1",
        description="django test project",
        contact=openapi.Contact(email="developer@notes.com"),
    ),
    public=True,
    permission_classes=[],
)

urlpatterns = [
    path("", status_view, name="status"),
    # path("notes/", NoteViewSet.as_view({"get": "list", "post": "create"}), name='notes'),
    # # path("notes/", notes_view, name='notes'),
    # # path("notes/<int:id>/", note_view, name='note'),
    # path("notes/<int:pk>/", NoteViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update"}),
    #      name='note')
    path("auth/", auth_view, name="auth"),
    path("profile/", profile_view, name="profile"),
    re_path("^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
] + router.urls
