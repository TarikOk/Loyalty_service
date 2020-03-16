from rest_framework import serializers
from django.contrib import admin
from django.urls import path, include
from accounting.views import *

urlpatterns = [
   path('client/create/', NewClient.as_view()),
   path('client/all/', ClientList.as_view()),
   path('client/detail/<int:pk>/', ClientDetail.as_view()),
   path('operations/all/', OperationsList.as_view()),
   path('operations/create/', NewOperation.as_view()),
   path('operations/detail/<int:pk>/', OperationDetail.as_view()),
]