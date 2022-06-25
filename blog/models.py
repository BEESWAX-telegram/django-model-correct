from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, related_name = 'author', on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date =  models.DateTimeField(auth_now_add=True)
    published_date = models.DateTimeField(auth_now_add=True)

    def _str_(self):
        return self.title
