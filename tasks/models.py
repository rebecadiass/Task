from django.db import models


class Task(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100, null=False, blank=False)
    completed = models.BooleanField(default=False)