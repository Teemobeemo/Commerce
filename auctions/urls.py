from django.urls import path

from . import views
from . import create_listings
from . import home_views
from . import listing
from . import close_listing_api
from . import watchlist
from . import add_to_watchlist_api
from . import category
from . import bid

urlpatterns = [
    path("", home_views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", create_listings.create_listing, name="create_listing"),
    path("listing", listing.listing, name="listing"),
    path("watchlist", watchlist.watchlist, name="watchlist"),
    path('category', category.category, name='category'),
    path("api/close", close_listing_api.close_listing_api,
         name='close_listing_api'),
    path("api/bid", bid.bid_api, name='bid_api'),
    path('api/watchlist', add_to_watchlist_api.add_to_watchlist,
         name='add_to_watchlist')
]
