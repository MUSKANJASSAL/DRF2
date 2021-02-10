from django.urls import path, include
from .import views
from rest_framework import routers
# Routers will take care of generating all the URLs from model

# Default page
router = routers.DefaultRouter()
router.register('languages', views.LanguageView)

urlpatterns = [
    path('', include(router.urls))
]