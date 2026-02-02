from django.db import models

# Create your models here.
class Todo(models.Model):

    class Status(models.TextChoices):
        NOT_STARTED = "NOT_STARTED", "Ej påbörjad"
        IN_PROGRESS = "IN_PROGRESS", "Pågående"
        FINISHED = "FINISHED", "Avklarad"

    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.NOT_STARTED,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.title