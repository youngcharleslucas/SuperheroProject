from django.urls import path
from . import views

app_name = 'superheros'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:hero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('delete_hero/<int:hero_id>/', views.delete_hero, name='delete_hero'),
    path('update_hero/<int:hero_id>/', views.update_hero, name='update_hero')
]