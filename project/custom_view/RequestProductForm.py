from django import forms

from custom_models.models import RequestProduct

class RequestProductForm(forms.ModelForm):
    class Meta:
        model = RequestProduct
        fields = ['name', 'email', 'phone', 'message', 'product', 'file_types']