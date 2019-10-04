from django.urls import path

from .views import listing, search, listings


urlpatterns = [
    path('', listings, name='listings'),
    path('<int:listing_id>', listing, name='listing'),
    path('search', search, name='search'),
]