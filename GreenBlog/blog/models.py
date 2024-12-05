from django.db import models

# Create your models here.


class Review(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    text = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name} - {self.email}'
