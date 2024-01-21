from django.db import models



class Myskill(models.Model):
    skillname=models.CharField(max_length=100)
    Degree=models.IntegerField(range(0,100))

    def __str__(self):
        return  f"{self.skillname} - {self.Degree}"
# Create your models here.
