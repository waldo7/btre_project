from django.shortcuts import render
from django.views import generic

from .choices import price_choices, bedroom_choices, state_choices
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


# def listing(request, listing_id):
#     return render(request, "listings/listing.html")
class ListingView(generic.DetailView):
    model = Listing
    template_name = "listings/listing.html"
    context_object_name = "listing"


def search(request):
    context = {
        "state_choices": state_choices,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices
    }
    return render(request, "listings/search.html", context)
