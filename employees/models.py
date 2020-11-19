from django.db import models
from areas.models import Area
from managers.models import Manager

class Employee(models.Model):
    name = models.CharField(max_length=255)
    id_card = models.IntegerField()
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    managers = models.ManyToManyField(Manager, related_name= 'employees', null=True)
    
    
    def __str__(self):
        return self.name
    
