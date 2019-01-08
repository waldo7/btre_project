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
    query_list = Listing.objects.order_by("-list_date")

    # keyword
    if "keywords" in request.GET:
        keywords = request.GET["keywords"].strip()
        if keywords:
            query_list = query_list.filter(
                description__icontains=keywords)

    # city
    if "city" in request.GET:
        city = request.GET["city"]
        if city:
            query_list = query_list.filter(
                city__iexact=city)

    # state
    if "state" in request.GET:
        state = request.GET["state"]
        if state:
            query_list = query_list.filter(
                state__iexact=state)

    # bedrooms
    if "bedrooms" in request.GET:
        bedrooms = request.GET["bedrooms"]
        if bedrooms:
            query_list = query_list.filter(
                bedrooms__gte=bedrooms)

    # price
    if "price" in request.GET:
        price = request.GET["price"]
        if price:
            query_list = query_list.filter(
                price__lte=price)

    context = {
        "state_choices": state_choices,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "listings": query_list,
        "values": request.GET
    }
    return render(request, "listings/search.html", context)
