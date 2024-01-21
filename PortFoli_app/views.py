from django.shortcuts import render
from .models import portfoli

def Portfoli_detail(request,id):
    portfoliid=portfoli.objects.get(id=id)
    return render(request,'PortFoli_app/PortFoli_Detail.html',{
        'porfolidetail':portfoliid
    })

# Create your views here.
