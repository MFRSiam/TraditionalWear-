from django import forms

class NameForm(forms.Form):
    Review= forms.IntegerField(max_value=10)
    Description = forms.TextInput()