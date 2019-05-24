"""models for posts"""

from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        """return posts username, title"""
        return 'User @{}, Post {}'.format(self.user.username, self.title)
    