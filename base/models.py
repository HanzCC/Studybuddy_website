from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User

# # Create your models here.

class User(AbstractUser):
    pass

# A topic can has multiple rooms, but a room only can has 1 topic 
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

# models by default hv the id generated for them.
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    # description can be empty / blank
    description = models.TextField(null=True, blank=True)
    # create many-to-many fields:
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    # room data that are auto created 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # class that decide the sequence of the ROOM - the latest the up.
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return str(self.name)
    

class Message(models.Model):
    # user template is provided by django
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
