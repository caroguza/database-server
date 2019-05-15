from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('key_value.urls')),
    path('admin/', admin.site.urls),
]
