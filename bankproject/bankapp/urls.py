from.import views
from django.urls import path
app_name='bankapp'
urlpatterns = [
    path('',views.demo,name='demo'),
    path('login/', views.login,name='login'),
    path('registration/',views.registrations,name='registration'),
    path('reglog/', views.reglog, name='reglog'),
    path('loginreg/', views.loginreg, name='loginreg'),
    path('', views.index,name='index'),
    path('logout/', views.logout, name='logout'),
]