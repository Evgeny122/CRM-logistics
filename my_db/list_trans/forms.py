from django import forms
from .models import Carrier, EditCarrier


class CarrierModelForm(forms.ModelForm):
    class Meta:
        model = Carrier
        exclude = []
        
class EditCarrierInTaskForm(forms.ModelForm):
    class Meta:
        model = EditCarrier
        exclude = ['tasks']