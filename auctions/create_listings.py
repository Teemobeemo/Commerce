from django.shortcuts import render, redirect
from .models import Listing
from .forms import NewListingForm
from django.contrib.auth.decorators import login_required

# Create a new listing


@login_required()
def create_listing(request):
    new_listing_form = NewListingForm(request.POST or None)
    if request.POST:
        if(new_listing_form.is_valid()):
            listing = new_listing_form.save(commit=False)
            listing.created_user = request.user
            listing.save()
            return redirect('index')

    return render(
        request, 'auctions/create-listing.html', {'new_listing_form': new_listing_form})
