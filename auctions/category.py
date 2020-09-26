from typing import List
from django.shortcuts import render,redirect
from .models import Listing

def category(request):
    category = request.GET.get('c')
    listings = None
    try:
        listings = Listing.objects.filter(category = category)
    
    except Listing.DoesNotExist:
        print(f'could not find {category}')

    return render(request,'auctions/category.html',{'listings':listings})
