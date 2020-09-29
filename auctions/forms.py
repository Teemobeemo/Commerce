from django import forms
from .models import Listing, Comment

CATEGORY_CHOICE = [
    ('Electronics', 'Electronics'),
    ('Home Appliances', 'Home Appliances'),
    ('Food and groceries', 'Food and groceries'),
    ('Outdoor', 'Outdoor'),
    ('Other', 'Other')
]


class NewListingForm(forms.ModelForm):
    # Add 'form-control' class to all.
    # To add id => {'class":'form-control','id':'YOUR ID GOES HERE'}
    title = forms.CharField(max_length=80, widget=forms.TextInput(
        attrs={'class': "form-control"}))
    description = forms.CharField(
        max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))
    starting_bid = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    image_url = forms.CharField(
        max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICE, widget=forms.RadioSelect)

    class Meta:
        model = Listing
        fields = [
            'title',
            'description',
            'starting_bid',
            'image_url',
            'category'
        ]


class NewCommentForm(forms.ModelForm):
    comment_text = forms.CharField(max_length=200)

    class Meta:
        model = Comment
        fields = [
            'comment_text'
        ]
