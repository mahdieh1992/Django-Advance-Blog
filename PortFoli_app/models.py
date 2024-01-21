from django.db import models

class portfoli(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    Image=models.ImageField(upload_to='Portfoli')
    Article=models.TextField(default='my article')

    def __str__(self):
        return f"{self.title} {self.description}"
# Create your models here.
