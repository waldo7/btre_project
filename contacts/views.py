from django.shortcuts import render, redirect
from django.contrib import messages

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

        contact = Contact(listing_id=listing_id, listing=listing, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        messages.success(
            request, "Thank you, your request has been submitted. A realtor will get back to you soon.")

        return redirect('listing', pk=listing_id)