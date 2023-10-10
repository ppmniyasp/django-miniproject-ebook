from django import forms
from .models import UserOrder
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserMessageForm(forms.ModelForm):
    class Meta:
        model = UserOrder
        fields = ['book_name', 'user']  


class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['first_name','username','email','password1','password2'] 
        labels = {
            'first_name': 'Name'

        }

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name != 'types':
                field.widget.attrs.update({'class': 'form-control'})