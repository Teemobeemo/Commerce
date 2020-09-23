from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import WatchList

@login_required()
def watchlist(request):
    user = request.user # Get current logged in user
    
    # Filter watchlist by the current user 
    watchlists = WatchList.objects.filter(user=user)

    # Set the listing array (list) to None
    listings = []

    # Add the listings to the watchlists
    for watchlist in watchlists:
        
        listings.append(watchlist.listing)

    return render(
        request,'auctions/watchlist.html',{'listings':listings})
