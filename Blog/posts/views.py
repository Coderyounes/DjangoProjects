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
    # OPTIMIZE: implement Pagination
    posts = Posts.objects.all()
    if posts:
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error': 'emtpy feeds'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_post(request):
    data = request.data
    # data['user'] = request.user.id # PS: use permission_classes isAuthenticated Decorator
    serializer = PostsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'New post Created'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_post(request, pk):
    try:
        post = Posts.objects.get(id=pk)
        if request.data.get('user') == post.user.id:
            serializer = PostsSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Article content'}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    except ObjectDoesNotExist:
        return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_post(request, pk):
    pass
