from django.urls import path
from . import views

urlpatterns = [
    path('', views.delivery_homepage, name='delivery_homepage'),
    path('list/', views.delivery_list, name='delivery_list'),
    path('add/', views.delivery_create, name='delivery_add'),
    path('update/<int:id>/', views.delivery_update, name='delivery_update'),
    path('delete/<int:id>/', views.delivery_delete, name='delivery_delete'),
]