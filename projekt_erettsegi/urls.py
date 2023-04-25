from django.contrib import admin
from django.urls import include, path

# mivel több applikációt is tervezünk, az adott kezdetű url-eket továbbirányítjuk az applikáció urls.py-ába. Az amúgy magától nem volt ott, létre kellett hozni.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('2022/okt/', include('app_22okt.urls')),
    path('2022/okt/legacy/', include('app_22oktlegacy.urls')),
]
