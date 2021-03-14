from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=256, default="")
    description = models.TextField(default="")


    def __str__(self):
        return self.text[:50]

