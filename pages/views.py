from django.shortcuts import render


from listings.models import Listing
from listings.choices import state_choices, bedroom_choices, price_choices
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }

    return render(request, 'pages/index.html', context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtor = Realtor.objects.filter(is_mvp=True)[0]

    context = {
        'realtors': realtors,
        'mvp_realtor': mvp_realtor
    }

    return render(request, 'pages/about.html', context)
