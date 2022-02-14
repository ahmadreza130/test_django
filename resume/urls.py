from django.urls import path
from . import views

urlpatterns = [ 
    path('create/', views.create),
    path('edit/', views.edit), 
    path('delete/', views.delete),
    path('get/', views.get),
    path('login/', views.login)
]
