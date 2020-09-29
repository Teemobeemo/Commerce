from django.shortcuts import render, redirect
from .models import Listing
from .forms import NewListingForm
from django.contrib.auth.decorators import login_required


@login_required()
def create_listing(request):
    """
    Get the new listing form with the data
    If no data then init with None
    """
    new_listing_form = NewListingForm(request.POST or None)

    # If POST Request
    if request.POST:
        # if form is vald
        if(new_listing_form.is_valid()):
            # Create a new listing
            listing = new_listing_form.save(commit=False)
            listing.created_user = request.user
            listing.save()
            return redirect('index')

    return render(
        request, 'auctions/create-listing.html', {'new_listing_form': new_listing_form})
