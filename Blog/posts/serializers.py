from rest_framework import serializers
from .models import Posts


class PostsSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Posts
        fields = '__all__'

    def get_author(self, obj):
        """
        method to fetch username from user instance
        return: username or None
        """
        if obj.user:
            return obj.user.username
        return None

    def validate_content(self, value):
        """
        Validate 'content' field length
        Return: raise ValidationError or return value
        """
        n = len(value)
        if n < 10 or n > 1000:
            raise serializers.ValidationError('Content length must be between 10 and 1000 characters')
        return value

    def validate(self, data):
        """
        Validate the existence of fields in data
        return: Raise ValidationError or return data
        """
        required = ['title', 'content', 'user']
        for field in required:
            if field not in data:
                raise serializers.ValidationError(f'{field} is required')
        return data

    def update(self, instance, validated_data):
        validated_data.pop('title', None)
        validated_data.pop('user', None)

        return super().update(instance, validated_data)