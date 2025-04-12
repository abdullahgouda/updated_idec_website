from django import forms

from custom_models.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']  # الحقول المراد تضمينها في الفورم
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'InputName',
                'placeholder': 'Your Name*',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'InputEmail',
                'placeholder': 'Email*',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'InputNumber',
                'placeholder': 'Phone Number',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'InputMessage',
                'rows': 5,
                'placeholder': 'Type your message',
            }),
        }
