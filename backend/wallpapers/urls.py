from django.urls import path

from .views import GenerateWallpaperView


urlpatterns = [
    path('generate/', GenerateWallpaperView.as_view(), name='generate-wallpaper'),
]