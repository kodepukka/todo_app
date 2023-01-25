from django.urls import path
from . import views

urlpatterns=[
    path('',views.godwin,name= 'godwin'),
    path('create',views.create, name= "create"),
    path('delete/<int:id>',views.delete, name= "delete")
]