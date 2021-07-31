from django.urls import path, include
from .views import AuthorViewSet, BookViewSet
from rest_framework.routers import DefaultRouter

router_author = DefaultRouter()
router_author.register('author', AuthorViewSet, basename='author')

router_book = DefaultRouter()
router_book.register('book', BookViewSet, basename='book')

urlpatterns = [
    path('author/', include(router_author.urls)),
    path('author/<int:pk>/', include(router_author.urls)),
    path('book/', include(router_book.urls)),
    path('book/<int:pk>/', include(router_book.urls)),
]