from django.urls import path
from . import views

app_name = "Chicago"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('registrar/cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('store/', views.store, name='store'),
]