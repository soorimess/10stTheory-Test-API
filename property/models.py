from django.db import models


class House(models.Model):
    title = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    area = models.IntegerField(blank=False)

    def __str__(self):
        return self.title

