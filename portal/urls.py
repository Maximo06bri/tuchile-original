from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.login_cliente, name='login'),
   
    path('dashboard/', views.dashboard, name='dashboard'),
    path('registro/', views.registro_cliente, name='registro'),

    path('logout/', views.logout_cliente, name='logout'),
    path('reserva/crear/', views.crear_reserva, name='crear_reserva'),
    path('pago/<int:reserva_id>/', views.pago_reserva, name='pago_reserva'),
    path('recuperar/', views.recuperar_password, name='recuperar'),
]
