from django.db import models


class Languages(models.Model):
    language = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.language
