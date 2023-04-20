from django.urls import path
from .views import feltolt_get, feltolt_post, index, feladat_2_kerdes, feladat_3_kerdes, feladat_4_kerdes, feladat_2_valasz, feladat_3_valasz, feladat_4_valasz, feladat_5_valasz, feladat_6_valasz

# most külön view-t kap a get és a post request.
# a tábla nevét így lehet elegánsan változóként kivenni az url-ből. 

urlpatterns = [
    path('', index),
    path('feltolt/<str:tabla>/', feltolt_get),
    path('feltolt/<str:tabla>/post/', feltolt_post),
    path('feladat/2/', feladat_2_kerdes),
    path('feladat/3/', feladat_3_kerdes),
    path('feladat/4/', feladat_4_kerdes),
    path('feladat/5/', feladat_5_valasz),
    path('feladat/6/', feladat_6_valasz),
    path('feladat/2/post/', feladat_2_valasz),
    path('feladat/3/post/', feladat_3_valasz),
    path('feladat/4/post/', feladat_4_valasz),
    path('feladat/5/post/', feladat_5_valasz),
    path('feladat/6/post/', feladat_6_valasz),

]
