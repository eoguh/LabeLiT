from django import forms

class InstanceForm(forms.Form):
    name = forms.CharField(max_length=100)
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
