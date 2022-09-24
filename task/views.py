from rest_framework import viewsets
from . import serializers
from . import models


class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TasksSerializer
    queryset = models.Tasks.objects.all()
    