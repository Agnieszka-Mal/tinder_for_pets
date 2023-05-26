from django.urls import path
from . import views
from .views import RegistrationView, login_user_view

app_name = 'users'
urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('login/', views.login_user_view, name='login')
]