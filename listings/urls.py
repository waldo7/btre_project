from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="listings"),
    path("", views.ListingsView.as_view(), name="listings"),
    path("<int:listing_id>", views.listing, name="listing"),
    path("search", views.search, name="search")

]
