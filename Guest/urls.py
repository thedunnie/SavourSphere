from django.urls import path
from Guest import views
app_name = 'Guest'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('Userreg/', views.user, name='user'),
]
