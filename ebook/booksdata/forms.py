from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Books, Review

class DateInput(forms.DateInput):
    input_type = 'date'

class AddBooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
        widgets = {
            'types': forms.CheckboxSelectMultiple, 
            'released':DateInput(),     
        }

    def __init__(self, *args, **kwargs):
        super(AddBooksForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name != 'types':
                field.widget.attrs.update({'class': 'input'})

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields = ['body'] 
        labels = {
            'body': 'Content',
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name != 'types':
                field.widget.attrs.update({'class': 'form-control'})

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['first_name','username','email','password1','password2'] 
        labels = {
            'first_name': 'Name'
        }


# class RegisterForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields = ['first_name','username','email','password1','password2'] 
#         labels = {
#             'first_name': 'Name'
#         }


# class SkillForm(ModelForm):
#     class Meta:
#         model = Skill
#         fields = '__all__'
#         exclude = ['owner']