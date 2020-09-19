from django import forms
from django.db.models.fields import PositiveIntegerField
from django.forms import fields
from django.forms import models
from .models import Listing,Comment

class NewListingForm(forms.ModelForm):
    title = forms.CharField(max_length=80)
    description = forms.CharField(max_length=500)
    starting_bid = forms.IntegerField()
    image_url = forms.CharField(max_length=500)
    
    class Meta:
        model=Listing
        fields = [
            'title',
            'description',
            'starting_bid',
            'image_url'
        ]

class NewCommentForm(forms.ModelForm):
    comment_text = forms.CharField(max_length=200)

    class Meta:
        model=Comment
        fields =[
            'comment_text'
        ]