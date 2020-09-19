from django.shortcuts import render
from .models import Listing,Comment
from .forms import NewCommentForm

def listing(request):
    listing_id = request.GET.get('id')
    listing = None
    comments = None

    # Check for new comments
    new_comment_form = NewCommentForm(request.POST or None)

    try:
        listing = Listing.objects.get(id = listing_id)
        
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
        'new_comment_form':new_comment_form
    })