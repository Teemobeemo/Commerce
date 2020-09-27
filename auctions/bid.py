from json.decoder import JSONDecodeError
import json
from django.db.models import Max
from auctions.models import Bid, Listing
from django.http.response import JsonResponse


def bid_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': "You should be logged in"})
    user = request.user
    rec_json =json.loads(request.body)

    listing_id = int(rec_json['id'])
    listing = None

    try:
        listing = Listing.objects.get(id=listing_id)
        bidding_amt = int(rec_json['amt'])

        all_bids = Bid.objects.filter(listing=listing)
        max_bid = all_bids.aggregate(Max('bidding_amount'))
        max_bid=(max_bid.get('bidding_amount__max'))

        if not max_bid:
            bid = Bid(listing=listing, bidding_user=user,bidding_amount=bidding_amt)
            bid.save()
            return JsonResponse({'success': 'ok','max_bid_amt':bidding_amt,'num_bid':1})
            
        if not bidding_amt >= max_bid:
            return JsonResponse({'error': "pay more than the highest current bid"})

        bid = Bid(listing=listing, bidding_user=user,bidding_amount=bidding_amt)
        bid.save()

        num_bid = Bid.objects.count()

        return JsonResponse({'success': 'ok','max_bid_amt':bidding_amt,'num_bid':num_bid})
    except Listing.DoesNotExist:
        return JsonResponse({'error': 'Can not find listing'})
