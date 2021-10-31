from django.urls import path
from . import views

app_name = 'superheros'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:hero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('<delete_heros/<hero_id>', views.delete_heros, name='delete_heros')
]