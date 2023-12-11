from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('car.urls')),
    path('api/', include('animal.urls')),
]
