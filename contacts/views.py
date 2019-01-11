from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contact
# Create your views here.


def contact(request):
    if request.method == "POST":
        listing_id = request.POST["listing_id"]
        listing = request.POST["listing"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        realtor_email = request.POST["realtor_email"]
        user_id = request.POST["user_id"]

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.filter(
                listing=listing, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already made this enquiry.")
                return redirect('listing', pk=listing_id)

        contact = Contact(listing_id=listing_id, listing=listing, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        # send_mail("subject", "message", "from", "receiptient")
        send_mail(
        'Property Listing Inquiry',
        'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
        'traversy.brad@gmail.com',
        [realtor_email, 'waldo.ramones@gmail.com'],
        fail_silently=False
        )

        messages.success(
            request, "Thank you, your request has been submitted. A realtor will get back to you soon.")

        return redirect('listing', pk=listing_id)
