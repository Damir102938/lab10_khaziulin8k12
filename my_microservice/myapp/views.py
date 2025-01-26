from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from rest_framework.exceptions import NotFound
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer

class TaskList(APIView):
    # Используем оба рендерера для JSON и браузерного интерфейса
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get(self, request):
        # Получаем все задачи
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({'tasks': serializer.data})

    def post(self, request):
        # Создаем новую задачу
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    # Используем оба рендерера для JSON и браузерного интерфейса
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise NotFound(detail="Задача не найдена")
        serializer = TaskSerializer(task)
        return Response({'task': serializer.data})

    def put(self, request, pk):
        # Полное обновление задачи
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise NotFound(detail="Задача не найдена")
        
        serializer = TaskSerializer(task, data=request.data, partial=False)  # False означает полное обновление
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        # Частичное обновление задачи
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise NotFound(detail="Задача не найдена")
        
        serializer = TaskSerializer(task, data=request.data, partial=True)  # True для частичного обновления
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Удаление задачи
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise NotFound(detail="Задача не найдена")
        
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)