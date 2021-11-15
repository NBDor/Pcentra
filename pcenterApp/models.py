from django.db import models
from .utils import create_url_shortcut

class Url(models.Model):
    shortcut = models.CharField(max_length=20, unique=True)
    full_link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f'{self.shortcut} to {self.full_link}'

    def save(self, *args, **kwargs):
        if not self.shortcut:
            self.shortcut = create_url_shortcut(self)

        super().save(*args, **kwargs)