from django.db import models


class Blog(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    Image=models.ImageField(upload_to='Blog/')

    def __str__(self):
        return f"{self.title} "
# Create your models here.
