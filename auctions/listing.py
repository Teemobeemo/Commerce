from django.shortcuts import render
from .models import Listing

def listing(request):
    listing_id = request.GET.get('id')
    listing = None

    try:
        listing = Listing.objects.get(id = listing_id)

    except Listing.DoesNotExist:
        print(f'Could not get listing where id = {listing_id}')

    return render(request,'auctions/listing.html',{
        'listing':listing
    })