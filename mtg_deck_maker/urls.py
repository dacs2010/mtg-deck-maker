from django.contrib import admin
from django.urls import include, path
from decks import views


urlpatterns = [
    # template paths
    path('', views.index, name='home'),
    # Admin paths
    path('admin/', admin.site.urls),
]
