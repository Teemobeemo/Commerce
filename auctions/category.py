from typing import List
from django.shortcuts import render, redirect
from .models import Listing

CATEGORY_CHOICE = [
    'Electronics',
    'Home Appliances',
    'Food and groceries',
    'outdoor',
    'Other'
]

def category(request):
    category = request.GET.get('c')

    if not category:
        return render(request,'auctions/category.html',{'categories':CATEGORY_CHOICE})

    listings = None
    try:
        listings = Listing.objects.filter(category=category)

    except Listing.DoesNotExist:
        print(f'could not find {category}')

    return render(request, 'auctions/category.html', {'listings': listings})
