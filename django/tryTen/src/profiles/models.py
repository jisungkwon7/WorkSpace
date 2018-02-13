from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default='description default text',blank=True,null=True)
    def __str__(self):
        return self.name
