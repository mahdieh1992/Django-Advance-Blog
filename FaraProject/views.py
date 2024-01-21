from django.shortcuts import render
from aboutme_app.models import Info
from PortFoli_app.models import portfoli
from ContactMe_app.models import contactme
from Skill_app.models import Myskill
from Blog_app.models import Blog
def home(request):
    myinfo=Info.objects.all().last()
    PortfoliObject = portfoli.objects.all()
    myskill=Myskill.objects.all()
    myBlog=Blog.objects.all()

    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        description=request.POST.get('comment')
        contactme.objects.create(name=name,Email=email,description=description)

    return render(request,'index.html',{
        'minfo':myinfo,
        'PortfoliObject': PortfoliObject,
        'myskill':myskill,
        'myBlog':myBlog


    })



