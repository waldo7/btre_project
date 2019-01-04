from django.shortcuts import render
from django.views import generic

from .models import Listing

# Create your views here.

# def index(request):
#     return render(request, "listings/listings.html", {"name": "waldo"})


class ListingsView(generic.ListView):
    model = Listing
    template_name = "listings/listings.html"
    context_object_name = "listings"


def listing(request, listing_id):
    return render(request, "listings/listing.html")


def search(request):
    return render(request, "listings/search.html")
