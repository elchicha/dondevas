from django.db import models

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)


    class Meta:
        verbose_name_plural = "ciudades"
    

    def __str__(self):
        return self.nombre