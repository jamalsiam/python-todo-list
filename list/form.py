from django import forms
class dataForm(forms.Form):
    name = forms.CharField(max_length = 20,
        widget=forms.TextInput(attrs={'class': 'inputField', 'placeholder': 'Name'}))
    location = forms.CharField(max_length = 20,
        widget=forms.TextInput(attrs={'class': 'inputField', 'placeholder': 'Location'}))