
from django.contrib import admin
from django.urls import path

from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView 
from actors.views import ActorCreateListView , ActorRetrieveUpdateDestroyView
from movies.views import MoviesCresteListView , MovieRetrieveUpdateDestroyView
from reviews.views import ReviewCreatelistView, ReviewRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/',GenreCreateListView.as_view(), name= 'genre-create-list'),
    path('genres/<int:pk>/',GenreRetrieveUpdateDestroyView.as_view(),name= 'genre-detail-view'),
    
    path('actors/', ActorCreateListView.as_view(), name = 'actor-create-list'),
    path('actors/<int:pk>/',ActorRetrieveUpdateDestroyView.as_view(),name = 'actor-datail-view'),
    
    path('movies/',MoviesCresteListView.as_view(),name = 'movie-create-list'),
    path('movies/<int:pk>/',MovieRetrieveUpdateDestroyView.as_view(),name= 'movie-detail-view'),
    
    path('reviews/', ReviewCreatelistView.as_view(), name = 'review-create-list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name ='review-detail-view'),
    

      
]
