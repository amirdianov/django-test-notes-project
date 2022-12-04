from rest_framework import serializers

from api.filelds import StdImageField
from web.models import Note, User, NoteComment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteComment
        fields = ('id', 'text')


class NoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    comments = CommentSerializer(many=True, read_only=True)
    text = serializers.CharField(write_only=True)

    image = StdImageField()

    def validate_title(self, value):
        return value.strip()

    def validate(self, attrs):
        # TODO set real user after auth implementation
        attrs['user_id'] = self.context['request'].user.id
        return attrs

    class Meta:
        model = Note
        fields = ('id', 'title', "text", 'user', 'image','comments', 'created_at')
