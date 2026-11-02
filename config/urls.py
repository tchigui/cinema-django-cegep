from django.contrib import admin
from django.urls import path
from cinema_app.views import accueilView, aproposView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", accueilView),
    path("apropos/", aproposView),
]