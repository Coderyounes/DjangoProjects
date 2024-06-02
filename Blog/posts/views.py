from django.shortcuts import render
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from posts.models import Posts
from .serializers import PostsSerializer


@api_view(['GET'])
def index(request):
    return Response({'message': 'Welcome to my Blog API'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def all_posts(request):
    posts = Posts.objects.all()
    if posts:
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error': 'emtpy feeds'}, status=status.HTTP_404_NOT_FOUND)

# TODO: view add posts
# TODO: view update post
# TODO: view Delete post
