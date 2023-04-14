from rest_framework import serializers

from api.filelds import StdImageField
from web.models import Note, User, NoteComment, Tag


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class TokenResponseSerializer(serializers.Serializer):
    token = serializers.CharField()


class StatusSerializer(serializers.Serializer):
    status = serializers.CharField()
    user_id = serializers.IntegerField()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "role", "name")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteComment
        fields = ("id", "text")


class NoteEditorSerializer(serializers.ModelSerializer):
    text = serializers.CharField()

    class Meta:
        model = Note
        fields = ("id", "text")
        read_only_fields = ("title",)

    def validate(self, attrs):
        # TODO set real user after auth implementation
        attrs["user_id"] = self.context["request"].user.id
        return attrs


class NoteSerializer(NoteEditorSerializer):
    user = UserSerializer(read_only=True)

    comments = CommentSerializer(many=True, read_only=True)
    text = serializers.CharField()

    image = StdImageField(allow_null=True, required=False)

    def validate_title(self, value):
        return value.strip()

    def validate(self, attrs):
        # TODO set real user after auth implementation
        attrs["user_id"] = self.context["request"].user.id
        return attrs

    class Meta:
        model = Note
        fields = ("id", "title", "text", "user", "comments", "image", "created_at")
        read_only_fields = ("title",)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "title")
