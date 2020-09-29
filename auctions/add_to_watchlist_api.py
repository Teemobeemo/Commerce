from auctions.watchlist import watchlist
from django.http import JsonResponse
from django.http import request
from .models import Listing, WatchList


def add_to_watchlist(request):
    # Check if user is logged in
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'You should be logged in!'})

    # Get the listing_id
    listing_id = request.GET.get('id')

    # Try to get the listing
    try:
        listing = Listing.objects.get(id=listing_id)
        user = request.user

        # Try and check if the watchlist already exists
        try:
            watchlist = WatchList.objects.get(listing=listing, user=user)
            return JsonResponse({'error': 'already watchlisted'})

        # User has not watchlisted it. Add it
        except WatchList.DoesNotExist:
            watchlist = WatchList()
            watchlist.user = user
            watchlist.listing = listing
            watchlist.save()
            return JsonResponse({'status': 'success'})

    # Error out if the listing does not exist
    except Listing.DoesNotExist:
        return JsonResponse({'error': 'Listing does not exist'})
