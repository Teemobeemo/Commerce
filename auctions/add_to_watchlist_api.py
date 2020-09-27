from auctions.watchlist import watchlist
from django.http import JsonResponse
from django.http import request
from .models import Listing, WatchList


def add_to_watchlist(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'You should be logged in!'})

    listing_id = request.GET.get('id')

    try:
        listing = Listing.objects.get(id=listing_id)
        user = request.user

        try:
            watchlist = WatchList.objects.get(listing=listing, user=user)
            return JsonResponse({'error': 'already watchlisted'})

        except WatchList.DoesNotExist:
            watchlist = WatchList()
            watchlist.user = user
            watchlist.listing = listing
            watchlist.save()
            return JsonResponse({'status': 'success'})

    except Listing.DoesNotExist:
        return JsonResponse({'error': 'Listing does not exist'})
