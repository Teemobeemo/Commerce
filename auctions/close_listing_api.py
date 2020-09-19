from django.http import JsonResponse
from django.http import request
from .models import Listing
def close_listing_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error':'You should be logged in!'})
    
    listing_id = request.GET.get('id')

    try:
        listing = Listing.objects.get(id = listing_id)
        listing.is_closed = True
        listing.save()
        return JsonResponse({'status':'listing closed!'})

    except Listing.DoesNotExist:
        return JsonResponse({'error':'Listing does not exist'})