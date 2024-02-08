from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name= 'Your  main stuff here')
    content = models.TextField(verbose_name='Your content here')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='when did they post')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
