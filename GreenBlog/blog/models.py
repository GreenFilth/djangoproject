from django.db import models

# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=40)
    text = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name} - {self.text}'


class postComment(models.Model):
    user_name = models.CharField(max_length=40)
    comment = models.CharField(max_length=150)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)