from django.urls import path
from . import views
from .api import ProfileList

urlpatterns = [
    path('', ProfileList.as_view()),
    path('<str:owner>/', views.profile, name='profile'),
]
