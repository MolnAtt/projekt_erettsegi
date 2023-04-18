from django.urls import path
from .views import feltolt_get, feltolt_post

# most külön view-t kap a get és a post request.
# a tábla nevét így lehet elegánsan változóként kivenni az url-ből. 

urlpatterns = [
    path('feltolt/<str:tabla>/', feltolt_get),
    path('feltolt/<str:tabla>/post/', feltolt_post),
]
