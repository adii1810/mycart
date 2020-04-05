
from django.conf.urls import url
from django.contrib import admin
from .import views
urlpatterns = [
    url("index/", views.index, name="ShopHome"),
    url("about/", views.about, name="AboutUs"),
    url("contact/", views.contact, name="ContactUs"),
    url("tracker/", views.tracker, name="TrackingStatus"),
    url("search/", views.search, name="Search"),
    url("products/<int:myid>", views.productView, name="ProductView"),
    url("checkout/", views.checkout, name="Checkout"),
    ]