from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import UserContact

def user_contacts(request):
    if request.method == 'POST':
        listing_id = request.POST['home_id']
        listing = request.POST['home']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        contact = UserContact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id
        )
        # Check if user has made inquire already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = UserContact.objects.filter(
                listing_id=listing_id,
                user_id=user_id
            )
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this lsiting')
                return redirect('/listings/' + listing_id)

        contact.save()

        # Send email
        # send_mail(
        #     'Property Listing Inquiry',
        #     'There has been an inquiry for ' + listing + '. Sign into to the dashboard for more info',
        #     'aulasmimocorporal@gmail.com',
        #     [realtor_email, 'mhiloca@gmail.com'],
        #     fail_silently=False
        # )

        messages.success(
            request,
            'Your inquire has been submitted, '
            'a realtor will get back to you asap'
        )

        return redirect('/listings/' + listing_id )
