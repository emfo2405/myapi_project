from django.db import models

# Create your models here.
class Todo(models.Model):

    class Status(models.TextChoices):
        NOT_STARTED = "NOT_STARTED", "Ej påbörjad"
        IN_PROGRESS = "IN_PROGRESS", "Pågående"
        FINISHED = "FINISHED", "Avklarad"

    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.NOT_STARTED
    )