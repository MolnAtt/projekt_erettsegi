from django.urls import path
from .views import index, feltolt_urlap, feltoltes_kerulet, feltoltes_varosresz, feltoltes_kapcsolat, feladat2, feladat3, feladat4, feladat5

# most külön view-t kap a get és a post request.
# a tábla nevét így lehet elegánsan változóként kivenni az url-ből. 

urlpatterns = [
    path('', index),
    path('feltoltes/kerulet/', feltolt_urlap),
    path('feltoltes/varosresz/', feltolt_urlap),
    path('feltoltes/kapcsolat/', feltolt_urlap),
    path('feladat/2/', feladat2),
    path('feladat/3/', feladat3),
    path('feladat/4/', feladat4),
    path('feladat/5/', feladat5),

    # path('feltoltes/<tabla:str>/post/', feltoltes), # egy lehetséges opció a szép egységes kezelésre...
    path('feltoltes/kerulet/post/', feltoltes_kerulet),
    path('feltoltes/varosresz/post/', feltoltes_varosresz),
    path('feltoltes/kapcsolat/post/', feltoltes_kapcsolat),

    
]
