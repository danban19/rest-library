from django.urls import path, include
from .views import AuthorViewSet, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('author', AuthorViewSet, basename='author')
router.register('book', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls))
]