from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

CATEGORY_CHOICE = [
    ('Electronics','Electronics'),
    ('Home Appliances','Home Appliances'),
    ('Food and groceries','Food and groceries'),
    ('outdoor','outdoor'),
    ('Other','Other')
]

class User(AbstractUser):
    pass

class Listing(models.Model):
    created_user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    starting_bid = models.PositiveIntegerField(default=0)
    image_url = models.CharField(max_length=500)
    is_closed = models.BooleanField(default=False)
    category = models.CharField(max_length=100,choices=CATEGORY_CHOICE,default='Other')

class Bid(models.Model):
    bidding_user = models.ForeignKey(User,default=1, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing,default=1, on_delete=models.CASCADE)
    bidding_amount = models.PositiveIntegerField(default=0)
    created_date = models.DateField(default=now)

class Comment(models.Model):
    comment_text = models.CharField(max_length=200,default='')
    user = models.ForeignKey(User,default=1, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing,default=1, on_delete=models.CASCADE)

class WatchList(models.Model):
    user = models.ForeignKey(User,default=1, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing,default=1, on_delete=models.CASCADE)
