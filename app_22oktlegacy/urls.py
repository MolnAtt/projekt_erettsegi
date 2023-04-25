from django.urls import path
from .views import index#, feltolt_get

# most külön view-t kap a get és a post request.
# a tábla nevét így lehet elegánsan változóként kivenni az url-ből. 

urlpatterns = [
    path('', index),
    # path('feltolt/<str:tabla>/', feltolt_get),
]
