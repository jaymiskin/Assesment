from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)



    def __str__(self):
        return self.title