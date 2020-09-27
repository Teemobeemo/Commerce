from django.shortcuts import render
from .models import Listing,Comment,Bid
from .forms import NewCommentForm
from django.db.models import Max

def listing(request):
    listing_id = request.GET.get('id')
    listing = None
    comments = None

    # Check for new comments
    new_comment_form = NewCommentForm(request.POST or None)

    max_bid = None

    try:
        listing = Listing.objects.get(id = listing_id)
        all_bids = Bid.objects.filter(listing=listing)
        max_bid = all_bids.aggregate(Max('bidding_amount'))
        max_bid=(max_bid.get('bidding_amount__max'))
        if request.POST:
            if new_comment_form.is_valid():
                comment = new_comment_form.save(commit=False)
                comment.user = request.user
                comment.listing = listing
                comment.save()

        comments = Comment.objects.filter(listing = listing)

    except Listing.DoesNotExist:
        print(f'Could not get listing where id = {listing_id}')

    return render(request,'auctions/listing.html',{
        'listing':listing,
        'comments':comments,
        'new_comment_form':new_comment_form,
        'max_bid':max_bid
    })