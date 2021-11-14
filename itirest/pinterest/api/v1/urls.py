from django.urls import path
from .view import hello, movie_list , movie_create ,movie_detail ,movie_delete , movie_update

app_name = 'pinterest-v1'
urlpatterns=[
    path('hello-api/<str:mykey>', hello, name='hello'),
    path('api/v1/movies/', movie_list, name='movie-list'),
    path('api/v1/movies/create', movie_create, name='movie-created'),
    path('api/v1/movies/<int:pk>', movie_detail, name='movie-details'),
    path('api/v1/movies/<int:pk>/delete', movie_delete, name='movie-delete'),
    path('api/v1/movies/<int:pk>/update', movie_update, name='movie-update'),
]
