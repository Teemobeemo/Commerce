from django.shortcuts import render
from .models import Listing


def index(request):
    # Get all listing!
    listings = Listing.objects.filter(is_closed=False)
    return render(request, "auctions/index.html", {'listings': listings})
