from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('cookbook/', include('cookbook.urls')),
]
