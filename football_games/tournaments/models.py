from django.db import models
from django.utils.timezone import now


class Tournament(models.Model):

    class Meta:
        verbose_name = 'Tournament'
        verbose_name_plural = 'Tournaments'

    title = models.CharField(max_length=50, unique=True)
    info = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/tournaments/', default='no-image.png')
    date_time = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return f'{self.title}'
