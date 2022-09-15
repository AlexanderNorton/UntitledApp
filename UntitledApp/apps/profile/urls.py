from django.urls import path
from . import views

urlpatterns = [
    path('<str:owner>/', views.profile, name='profile'),
]
