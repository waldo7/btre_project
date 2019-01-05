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
    paginate_by = 6
    # queryset = Listing.objects.all()
    # ordering = ["-list_date"]

    def get_queryset(self):
        return Listing.objects.order_by("-list_date").filter(is_published=True)


def listing(request, listing_id):
    return render(request, "listings/listing.html")


def search(request):
    return render(request, "listings/search.html")
