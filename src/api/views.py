import time

from django.db.models import Prefetch
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from api.serializers import NoteSerializer, StatusSerializer, NoteEditorSerializer
from web.models import Note, NoteComment
from web.services import share_note


@swagger_auto_schema(method="GET", operation_id="api_status", responses={status.HTTP_200_OK: StatusSerializer()})
@api_view()
@permission_classes([])
def status_view(request):
    """Проверить API"""
    time.sleep(10)
    return Response(StatusSerializer({"status": "ok", "user_id": request.user.id}).data)


class NoteViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return NoteEditorSerializer

        if self.action == "share":
            return None
        return NoteSerializer

    def get_queryset(self):
        return (
            Note.objects.all()
            .optimize_for_lists()
            .prefetch_related(Prefetch("comments", NoteComment.objects.all().order_by("created_at")))
            .filter(user=self.request.user)
        )

    @action(
        methods=["POST"],
        # detail=True /notes/{id}/share/
        # detail=False /notes/share/
        detail=True,
    )
    def share(self, request, *args, **kwargs):
        note = self.get_object()
        share_note(note)
        return Response({"status": "ok"})


# @api_view(['GET', 'POST'])
# def notes_view(request):
#     if request.method == 'POST':
#         serializer = NoteSerializer(
#             data=request.data,
#             context={"request": request},
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     notes = Note.objects.all().optimize_for_lists().prefetch_related(
#         Prefetch('comments', NoteComment.objects.all().order_by("created_at"))
#     )
#     serializer = NoteSerializer(notes, many=True)
#     return Response(serializer.data)

#
# @api_view(['GET', 'PUT'])
# def note_view(request, id):
#     note = get_object_or_404(Note, id=id)
#     if request.method == "PUT":
#         serializer = NoteSerializer(
#             instance=note,
#             data=request.data,
#             context={"request": request}
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     serializer = NoteSerializer(note)
#     return Response(serializer.data)
