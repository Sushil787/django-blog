from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title= models.TextField()
    body= models.TextField()
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.TextField()

    def __str__(self) -> str:
        return self.title
