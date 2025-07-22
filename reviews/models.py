# reviews/models.py
from django.db import models

class Review(models.Model):
    product = models.CharField(max_length=100)
    sentiment = models.CharField(max_length=10)
    text = models.TextField()

    def __str__(self):
        return f"{self.product} - {self.sentiment}"
