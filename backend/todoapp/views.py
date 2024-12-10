from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from rest_framework.response import Response
from .models import TodoItem
from .serializers import TodoItemSerializer

# Create your views here.

# Heartbeat request
def Heartbeat(request):
    return JsonResponse({'status': 'Backend is active'})

class TodoListView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        todos = TodoItem.objects.all()
        serializer = TodoItemSerializer(todos, many=True)
        return Response(serializer.data)
    
    def delete(self, request, *args, **kwargs):
        TodoItem.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TodoDetailView(APIView):
    def patch(self, request, *args, **kwargs):
        try:
            todo = TodoItem.objects.get(id=kwargs['pk'])
        except TodoItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = TodoItemSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)