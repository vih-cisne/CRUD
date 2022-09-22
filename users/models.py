from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=None)
    email = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.name

