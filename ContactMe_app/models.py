from django.db import models

class contactme(models.Model):
    name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100,null=True)
    description=models.TextField(null=True)


    def __str__(self):
        return f"{self.name} - {self.description}"