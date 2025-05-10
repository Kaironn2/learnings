from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarsView, NewCarView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', CarsView.as_view(), name='cars_list'),
    path('new_car', NewCarView.as_view(), name='new_car'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
