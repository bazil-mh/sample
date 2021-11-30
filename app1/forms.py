
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    check_field = forms.CharField(label='field test', max_length=100)
