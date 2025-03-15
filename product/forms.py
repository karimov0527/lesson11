from django import forms
from .models import Waters

class Water_Form(forms.ModelForm):
    class Meta :
        model = Waters
        fields = "__all__"


        