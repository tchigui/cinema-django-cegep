from django.contrib import admin
from django.urls import path
from cinema_app.views import accueilView, filmsView, aproposView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", accueilView),
    path("films/", filmsView),
    path("apropos/", aproposView),
]