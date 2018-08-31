from django.db import models
from django_extensions.db.models import TimeStampedModel


class Todo(TimeStampedModel):
    name = models.CharField(max_length=256)
