from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class Pet(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50, choices=[('dog', 'Dog'), ('cat', 'Cat')])
    breed = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50, choices=[('dog', 'Dog'), ('cat', 'Cat')])

    def __str__(self):
        return self.name


class Forum(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title