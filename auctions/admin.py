from django.contrib import admin
from .models import Comment, Listing, Bid

# Registering the models here for Django Admin Site
admin.site.register(Comment)
admin.site.register(Listing)
admin.site.register(Bid)
