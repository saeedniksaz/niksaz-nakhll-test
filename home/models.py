from django.db import models


class Mahsoul(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    old_price = models.IntegerField()

    def __str__(self):
        return self.name