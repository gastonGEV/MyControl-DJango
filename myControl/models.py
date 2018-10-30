from django.db import models
from django.utils import timezone


# class Post(models.Model):
#     author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(
#         default=timezone.now)
#     published_date = models.DateTimeField(
#         blank=True, null=True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title


class Tipo(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class MedPago(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Incidencia(models.Model):
    title = models.CharField(max_length=200)
    mount = models.IntegerField()
    desc = models.CharField(max_length=200)
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tipo = models.ForeignKey('Tipo', on_delete=models.CASCADE)
    medPago = models.ForeignKey('MedPago', on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.title