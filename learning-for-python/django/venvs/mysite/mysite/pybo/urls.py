from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index), # pybo/ URL에 접속하면 index 함수가 호출됨
]