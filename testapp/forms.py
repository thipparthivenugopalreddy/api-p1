from django import forms
from .models import *

class empform(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
