from django.urls import path
from .views import author_list, author_detail, AuthorView, AuthorDetails

urlpatterns = [
    path('author/', AuthorView.as_view()),
    path('detail/<int:id>/', AuthorDetails.as_view()),

]