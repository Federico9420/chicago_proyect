from django.urls import path
from . import views

app_name = "Store"

urlpatterns = [
    path('index_store', views.index_store, name='index_store'),
    path('cart', views.cart, name= 'cart'),
    path('category/<str:category_name>/', views.category_view, name='category_view'), 
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),         
               
]
