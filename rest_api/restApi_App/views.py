from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


def redirect(request):
    return render(request, "redirect.html")

class PostList(generics.ListCreateAPIView):
    serializer_class = ItemSerializers


    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(itemLocation=location)
        return queryset
    

class PostDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ItemSerializers
    queryset = Item.objects.all()
