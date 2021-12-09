from django import forms
from django.forms import widgets

from .models import Topping

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['text']
        labels = {'text':''}

        # A widget is a HTML form element, such as a single-line text box,
        # multi-line text area, or drop down list.
        # Customize the input widget for the field "text" so the text area
        # will be 30 columns wide instead of the default 40
        widgets = {'text': forms.Textarea(attrs={'cols': 30})}

        