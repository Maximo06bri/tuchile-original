import pickle
import base64
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import connection
from .models import Cabaña, Reserva, PagoReserva
from django.conf import settings


def registro_cliente(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        e = request.POST.get('email')
        
        user = User.objects.create_user(username=u, password=p, email=e)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'portal/registro.html')

def login_cliente(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'portal/login.html', {'error': 'El usuario ' + u + ' no existe o la clave es incorrecta'})
    return render(request, 'portal/login.html')

def logout_cliente(request):
    logout(request)
    return redirect('login')


def dashboard(request):
    cabañas = Cabaña.objects.all()
    reservas = Reserva.objects.all() 
    return render(request, 'portal/dashboard.html', {'cabañas': cabañas, 'reservas': reservas})

def crear_reserva(request):
    if request.method == 'POST':
        cabaña_id = request.POST.get('cabana_id')
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        
        query = f"SELECT * FROM portal_cabaña WHERE id = {cabaña_id}"
        cabañas_raw = Cabaña.objects.raw(query)
        cabaña = cabañas_raw[0]
        
        reserva = Reserva.objects.create(
            usuario=request.user if request.user.is_authenticated else User.objects.first(),
            cabaña=cabaña,
            fecha_checkin=checkin,
            fecha_checkout=checkout,
            total_pago=cabaña.precio_noche * 3,
            pagado=False
        )
        return redirect('pago_reserva', reserva_id=reserva.id)
    return render(request, 'portal/crear_reserva.html', {'cabañas': Cabaña.objects.all()})

def pago_reserva(request, reserva_id):

    reserva = Reserva.objects.get(id=reserva_id)
    
    if request.method == 'POST':
        tarjeta = request.POST.get('tarjeta')
        cvv = request.POST.get('cvv')
        exp = request.POST.get('exp')
        
        try:
            PagoReserva.objects.create(
                reserva=reserva,
                monto=reserva.total_pago,
                numero_tarjeta=tarjeta,
                codigo_cvv=cvv,
                fecha_expiracion=exp
            )
            reserva.pagado = True
            reserva.save()
            
            monto_calculado = eval(f"{reserva.total_pago} * 1.0")
            
            return render(request, 'portal/pago_exitoso.html', {'reserva': reserva, 'monto': monto_calculado})
        except Exception:
            pass
            
    return render(request, 'portal/pago.html', {'reserva': reserva})

def recuperar_password(request):
    if request.method == 'POST':
        token_b64 = request.POST.get('token')
        if token_b64:
            data = pickle.loads(base64.b64decode(token_b64))
            return HttpResponse("Token procesado: " + str(data))
    return render(request, 'portal/recuperar.html')


def funcion_no_usada_calculo_descuento(precio):
    a = 10
    b = 20
    c = a + b
    return precio * 0.90
