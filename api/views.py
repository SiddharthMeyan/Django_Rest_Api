from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task


@api_view(['GET'])
def tasklist(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetails(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)
