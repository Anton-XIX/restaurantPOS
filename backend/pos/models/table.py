from django.db import models


class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    is_active = models.BooleanField(default=True)
    comment = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'Table №{self.number}'
