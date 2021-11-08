#created this document using https://docs.djangoproject.com/en/3.2/topics/forms/

from django import forms

class SuggestedListingName(forms.Form):
    name = forms.CharField(label='Name of housing option:', max_length=200)

class SuggestedListingAddress(forms.Form):
    address = forms.CharField(label='Address:', max_length=500)