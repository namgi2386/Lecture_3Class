from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Todo
from .serializers import TodoSerializer, TodoListSerializer

# Create your views here.
@api_view(['GET',"POST"])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["DELETE","GET"])
def todo_detail(request, todo_pk):
    todo = get_object_or_404(Todo,pk=todo_pk)
    if request.method == "DELETE":
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == "GET":
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
