from django.db import models

class bitacora(models.Model):
    actividad = models.CharField(max_length=200)
    user = models.CharField(max_length=30)
    
