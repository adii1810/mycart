
from django.conf.urls import url
from django.contrib import admin
from .import views
urlpatterns = [
   # url(r'^admin/', admin.site.urls),
    url("", views.index, name="blogHome"),
    url("about/", views.about, name="AboutUs"),
    url("contact/", views.contact, name="ContactUs"),
    url("tracker/", views.tracker, name="TrackingStatus"),
    url("search/", views.search, name="Search"),
    url("productview/", views.productView, name="ProductView"),
    url("checkout/", views.checkout, name="Checkout"),
    ]