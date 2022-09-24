from django.db import models
from uuid import uuid4


class Tasks(models.Model):
    task_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    task_name = models.CharField(max_length=255)
    task_created_at = models.DateField(auto_now_add=True)
    task_is_done = models.BooleanField(default=False)
