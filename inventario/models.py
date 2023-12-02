from django.db import models


   
class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=15)

    def __str__(self):
        return self.estado

class TipoCarro(models.Model):
    id_tp_carro = models.AutoField(primary_key=True)
    tipo_carro = models.CharField(max_length=15)

    def __str__(self):
        return self.tipo_carro


class Cabina(models.Model):
    id_cabina = models.AutoField(primary_key=True)
    nombre_cabina = models.CharField(max_length=15)
    item = models.IntegerField()
    elemento = models.CharField(max_length=30)
    marca = models.CharField(max_length=30, null=True)
    observaciones = models.CharField(max_length=100, null=True)
    cantidad = models.IntegerField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    
class Carro(models.Model):
    id_carro = models.AutoField(primary_key=True)
    id_tp_carro = models.ForeignKey(TipoCarro, on_delete=models.CASCADE)
    id_cabina = models.ForeignKey(Cabina, on_delete=models.CASCADE)

# Create your models here.
