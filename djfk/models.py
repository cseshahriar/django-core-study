from django.db import models
from django.conf import settings 

User = settings.AUTH_USER_MODEL # 'auth.User'  

# ForeignKey is a many-to-one relationship 
class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    # passenders = models.ManyToManyField(User) # on_delete 
    # first_user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) # unique  
    # drivers = models.ManyToManyField(User)   
    name = models.CharField(max_length=50)  

    def __str__(self):
        return self.name  
