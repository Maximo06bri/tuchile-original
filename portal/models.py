from django.db import models
from django.contrib.auth.models import User

class Cabaña(models.Model):
    nombre = models.CharField(max_length=100)
    zona = models.CharField(max_length=50) # 'Costera' o 'Sur'
    precio_noche = models.DecimalField(max_digits=10, decimal_places=2)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cabaña = models.ForeignKey(Cabaña, on_delete=models.CASCADE)
    fecha_checkin = models.DateField()
    fecha_checkout = models.DateField()
    total_pago = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.BooleanField(default=False)
    
    comentario_cliente = models.TextField(blank=True, null=True)

class PagoReserva(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    numero_tarjeta = models.CharField(max_length=16)
    codigo_cvv = models.CharField(max_length=4)
    fecha_expiracion = models.CharField(max_length=7)
    fecha_transaccion = models.DateTimeField(auto_now_add=True)
