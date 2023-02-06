from django.db import models

# Create your models here.
class Notes(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    createdAt=models.DateTimeField(auto_now_add=True)