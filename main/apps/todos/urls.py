from django.urls import path, include
from rest_framework import routers

from main.apps.todos import viewsets

router = routers.DefaultRouter()
router.register("todos", viewsets.TodoViewset, base_name="todos")

urlpatterns = [
    path("", include(router.urls))
]