from django.urls import path
from .views import *

urlpatterns = [
    
    path('api/', PostList.as_view()),
    path('api/<int:pk>/', PostDetail.as_view()),
]