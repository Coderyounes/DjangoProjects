from rest_framework import serializers
from .models import Posts


class PostsSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Posts
        fields = '__all__'

    def get_author(self, obj):
        if obj.user:
            return obj.user.username
        return None
    def validate_content(self, value):
        n = len(value)
        if n < 10 or n > 1000:
            raise serializers.ValidationError('Content length must be between 10 and 1000 characters')
        return value