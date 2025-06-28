from django.db import models

# Create your models here.

class post (models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=2000)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} {self.author}"

