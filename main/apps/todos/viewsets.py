from rest_framework import viewsets

from main.apps.todos.models import Todo
from main.apps.todos.serializers import TodoSerializer


class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer