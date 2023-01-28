from django.urls import path
from . import views

urlpatterns=[
    path('',views.godwin,name= 'godwin'),
    path('create',views.create, name= "create"),
    path('delete/<int:id>',views.delete, name= "delete"),
    path('update/<int:id>',views.update, name= "update"),
    path('completed/<int:id>',views.completed, name= "completed"),
]
