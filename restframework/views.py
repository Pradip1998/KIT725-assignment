from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *

# Create your views here.
@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'List' : '/task-list/',
        'Detail View' : '/task-detail/<str:pk>',
        'Create' : '/task-created/',
        'Update': '/task-updated/<stk:pk>',
        'Delete': '/task-deleted/<stk:pk>',

    }
    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    if request.user.is_authenticated:
        Products = Product.objects.all()
        serializer = TaskSerializer(Products, many=True)
        return Response(serializer.data)
    else:
        return Response("You Must Log in")
