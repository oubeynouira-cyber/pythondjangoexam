from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #homepage
    path('', views.delivery_homepage, name='delivery_homepage'),
    #auth
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    #delivery
    path('deliveries/', views.delivery_list, name='delivery_list'),
    path('deliveries/add/', views.delivery_create, name='delivery_add'),
    path('deliveries/update/<int:id>/', views.delivery_update, name='delivery_update'),
    path('deliveries/delete/<int:id>/', views.delivery_delete, name='delivery_delete'),
    path('deliveries/<int:id>/detail/', views.delivery_detail, name='delivery_detail'),
    path('deliveries/<int:id>/deliver/', views.delivery_mark_delivered, name='delivery_mark_delivered'),
    #suppliers
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/add/', views.supplier_create, name='supplier_add'),
    path('suppliers/update/<int:id>/', views.supplier_update, name='supplier_update'),
    path('suppliers/delete/<int:id>/', views.supplier_delete, name='supplier_delete'),
    #clients
    path('clients/', views.client_list, name='client_list'),
    path('clients/add/', views.client_create, name='client_add'),
    path('clients/update/<int:id>/', views.client_update, name='client_update'),
    path('clients/delete/<int:id>/', views.client_delete, name='client_delete'),
    #products
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_create, name='product_add'),
    path('products/update/<int:id>/', views.product_update, name='product_update'),
    path('products/delete/<int:id>/', views.product_delete, name='product_delete'),

   ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)