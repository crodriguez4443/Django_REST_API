from django.db import models

class Pants(models.Model):
    name = models.CharField(max_length=100)
    fabric = models.CharField(max_length=100)
    quantity = models.IntegerField()
    four_way_stretch = models.BooleanField()
    price = models.IntegerField()

    def __str__(self):
        return self.name