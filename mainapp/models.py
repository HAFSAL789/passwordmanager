from django.db import models
from django.contrib.auth.models import User


class AddItem(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    Title = models.CharField(max_length=150)
    password = models.CharField(max_length=200)


    def __str__(self):
        return self.Title