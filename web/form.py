from django import forms
from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'email', 'mobilenumber', 'age', 'qualification', 'location', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'mobilenumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Mobile Number'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Your Age'}),
            'qualification': forms.Select(attrs={'class': 'form-control nice-select', 'placeholder': 'Your Qualification'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Location'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 4}),
        }