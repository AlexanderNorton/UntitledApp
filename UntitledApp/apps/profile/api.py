from django.shortcuts import render
from .serializers import ProfileSerializer
from rest_framework import mixins
from rest_framework import generics
from .models import Profile

# Create your views here.


class ProfileList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
