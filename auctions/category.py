from typing import List
from django.shortcuts import render, redirect
from .models import Listing

# List of Categories
CATEGORY_CHOICE = [
    'Electronics',
    'Home Appliances',
    'Food and groceries',
    'Outdoor',
    'Other'
]

def category(request):
    # Get the specific category
    category = request.GET.get('c')

    # If it does not exist then send over the list of categories
    if not category:
        return render(request,'auctions/category.html',{'categories':CATEGORY_CHOICE})

    listings = None

    # Get the listings with the specific category
    try:
        listings = Listing.objects.filter(category=category,is_closed=False)

    except Listing.DoesNotExist:
        print(f'could not find {category}')

    return render(request, 'auctions/category.html', {'listings': listings})
