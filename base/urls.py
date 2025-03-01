from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.signup,name='signup'),
    path('login-page/',views.loginPage,name='loginPage'),
    path('home/',views.home,name='home'),
    path('edit/<int:pk>',views.editwatchlist,name='edit-watchlist'),
    path('delete/<int:pk>',views.deletewatchlist,name='delete-watchlist'),
    path('movies/<int:pk>',views.movies,name='movies'),
    path('status/<int:pk>',views.status,name='status'),
    path('editmovie/<int:pk>',views.editmovie,name='editmovie'),
    path('deletemovie/<int:pk>',views.deletemovie,name='deletemovie'),
    path('recommend/<int:pk>',views.recommend,name='recommend'),
    path('add/<str:movie>',views.add,name='add'),
    path('signout/',views.signout,name='signout'),
]
