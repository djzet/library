from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'book', views.BookViewSet)
router.register(r'author', views.AuthorViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.

urlpatterns = [
   path('', include(router.urls)),
   path('auth/', include('rest_framework.urls'))
]
