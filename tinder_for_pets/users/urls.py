from django.urls import path
from . import views
from .views import RegistrationView, LoginUsersView

app_name = 'users'
urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginUsersView.as_view(), name='login')
]