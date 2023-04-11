from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User

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
        fields = ['username', 'email']