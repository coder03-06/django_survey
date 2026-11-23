
from django import forms
from .models import SurveyResponse


class SurveyForm(forms.ModelForm):

    class Meta:
        model = SurveyResponse

        fields = [
            'name',
            'email',
            'technology',
            'rating',
            'feedback',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your name'
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email'
            }),

            'technology': forms.Select(),

            'rating': forms.Select(),

            'feedback': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Your feedback'
            }),
        }
