from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from .models import Person


@api_view(['GET'])
def profile(request):
    try:
        current = Person.objects.get(user=request.user)
    except ObjectDoesNotExist:
        return Response({'error': 'no such user'}, status=status.HTTP_404_NOT_FOUND)
    res = {
        'username': current.user.username,
        'firstname': current.user.first_name
    }
    return Response(res, status=status.HTTP_200_OK)

