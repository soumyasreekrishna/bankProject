from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('preform/', views.preform, name='preform'),
    path('form1/', views.addForm, name='form1'),
    path('success/', views.success, name='success'),

]