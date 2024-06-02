from rest_framework import serializers
from .models import Comments


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comments
        fields = '__all__'

    def get_author(self, obj):
        if obj.user:
            return obj.user.username
        return None
