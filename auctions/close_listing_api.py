from django.http import JsonResponse
from django.http import request
from .models import Listing


def close_listing_api(request):
    # Check if user logged in
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'You should be logged in!'})

    # Get listing id
    listing_id = request.GET.get('id')

    # Try to get the listing. Then close it
    try:
        listing = Listing.objects.get(id=listing_id)
        if not listing.created_user.id is request.user.id:
            return JsonResponse({"error":"not your listing"})
        listing.is_closed = True
        listing.save()
        return JsonResponse({'status': 'listing closed!'})

    except Listing.DoesNotExist:
        return JsonResponse({'error': 'Listing does not exist'})
