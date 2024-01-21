from django.urls import path
from . import views
urlpatterns=[
    path('detail/<int:id>',views.Portfoli_detail)
]