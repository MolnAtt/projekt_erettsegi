from django.urls import path
from .views import feltolt_get, feltolt_post, index, feladat_2_get, feladat_3_get, feladat_4_get, feladat_5_get, feladat_6_get, feladat_2_post, feladat_3_post, feladat_4_post, feladat_5_post, feladat_6_post

# most külön view-t kap a get és a post request.
# a tábla nevét így lehet elegánsan változóként kivenni az url-ből. 

urlpatterns = [
    path('', index),
    path('feltolt/<str:tabla>/', feltolt_get),
    path('feltolt/<str:tabla>/post/', feltolt_post),
    path('feladat/2/', feladat_2_get),
    path('feladat/3/', feladat_3_get),
    path('feladat/4/', feladat_4_get),
    path('feladat/5/', feladat_5_get),
    path('feladat/6/', feladat_6_get),
    path('feladat/2/post/', feladat_2_post),
    path('feladat/3/post/', feladat_3_post),
    path('feladat/4/post/', feladat_4_post),
    path('feladat/5/post/', feladat_5_post),
    path('feladat/6/post/', feladat_6_post),

]
