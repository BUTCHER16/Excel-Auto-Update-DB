from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_excel, name='home'),
    path('success/', views.success_view, name='success'),
    
]
