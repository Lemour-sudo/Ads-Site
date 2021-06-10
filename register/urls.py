from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('', views.SignUpView.as_view(), name='signup')
]