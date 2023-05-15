from django.urls import path
from .views import index, feltolt_urlap, feltoltes_kerulet, feltoltes_varosresz

# most külön view-t kap a get és a post request.
# a tábla nevét így lehet elegánsan változóként kivenni az url-ből. 

urlpatterns = [
    path('', index),
    path('feltoltes/kerulet/', feltolt_urlap),
    path('feltoltes/varosresz/', feltolt_urlap),

    # path('feltoltes/<tabla:str>/post/', feltoltes), # egy lehetséges opció a szép egységes kezelésre...
    path('feltoltes/kerulet/post/', feltoltes_kerulet),
    path('feltoltes/varosresz/post/', feltoltes_varosresz),

    
]
