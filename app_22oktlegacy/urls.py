from django.urls import path
from .views import index, kerulet_feltolt_urlap, feltoltes_kerulet

# most külön view-t kap a get és a post request.
# a tábla nevét így lehet elegánsan változóként kivenni az url-ből. 

urlpatterns = [
    path('', index),
    path('feltoltes/kerulet/', kerulet_feltolt_urlap),
    path('feltoltes/kerulet/post/', feltoltes_kerulet),
]
