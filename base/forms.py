from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Room

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

## Create form for the Room
class RoomForm(ModelForm):
    class Meta:
        # model that want to create a room for 
        model = Room
        # create the form's fields based on models.py object ['host', 'name', 'topic', 'description']
        fields = '__all__'
        exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name', 'username', 'email', 'bio']