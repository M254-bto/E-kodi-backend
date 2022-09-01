from django.db import models
from django.contrib.auth.models import User
from landlord.models import Appartments

class Tenant(User,models.Model):
    appartment = models.ForeignKey(Appartments, on_delete=models.CASCADE, null=True, related_name='appartment')
    contact = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Tenant'
        verbose_name_plural = 'Tenants'
    

