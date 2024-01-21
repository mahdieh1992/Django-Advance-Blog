from django.db import models


class Info(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='Info/',null=True)


    def __str__(self):
        return f"{self.title} - {self.description}"