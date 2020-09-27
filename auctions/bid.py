from json.decoder import JSONDecodeError
import json
from django.db.models import Max
from auctions.models import Bid, Listing
from django.http.response import JsonResponse


def bid_api(request):
    user = request.user

    # Check if user is authenticated
    if not user.is_authenticated:
        return JsonResponse({'error': "You should be logged in"})
    
    # Get the payload
    rec_json = json.loads(request.body)

    listing_id = int(rec_json['id'])
    listing = None

    # Try to get the listing and process
    try:
        listing = Listing.objects.get(id=listing_id)
        bidding_amt = int(rec_json['amt'])

        # Get all Bids of the current post
        all_bids = Bid.objects.filter(listing=listing)

        # Get the max bidding amount
        max_bid = all_bids.aggregate(Max('bidding_amount'))
        max_bid = (max_bid.get('bidding_amount__max'))

        # If there is no max_bid then add this
        if not max_bid:
            bid = Bid(listing=listing, bidding_user=user,
                      bidding_amount=bidding_amt)
            bid.save()
            return JsonResponse({'success': 'ok', 'max_bid_amt': bidding_amt, 'num_bid': 1})

        # If there is a max bid then check if the current amt is larger than the max bid
        if not bidding_amt >= max_bid:
            return JsonResponse({'error': "pay more than the highest current bid"})

        # save the bid
        bid = Bid(listing=listing, bidding_user=user,
                  bidding_amount=bidding_amt)
        bid.save()

        # Get all the number of bid(s)
        num_bid = Bid.objects.count()

        return JsonResponse({'success': 'ok', 'max_bid_amt': bidding_amt, 'num_bid': num_bid})
    
    # Error out if the listing does not exist
    except Listing.DoesNotExist:
        return JsonResponse({'error': 'Can not find listing'})
