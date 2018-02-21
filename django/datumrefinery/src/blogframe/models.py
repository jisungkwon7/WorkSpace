from django.db import models
# Create your models here.

class profile(models.Model):
    firstname = models.CharField(max_length=120,blank=True,null=True)
    lastname = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.Lastname
