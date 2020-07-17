from django.urls import path

from . import views

app_name = 'messageboard'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.board_topics, name='topics')
]
