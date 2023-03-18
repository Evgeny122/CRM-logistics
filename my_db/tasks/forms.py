from django import forms
from .models import Tasks, Comments


class AddTasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = [
            'logist',
            'status',
            'route',
            'cargo',
            'transport_requirement',
            'price_client',
            
        ]

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            'text'
        ]

