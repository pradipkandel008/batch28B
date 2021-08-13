from django import forms


class PersonForm(forms.Form):
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    dob = forms.DateField()
    phone = forms.IntegerField()
    address = forms.CharField(max_length=200)