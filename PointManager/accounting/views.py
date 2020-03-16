from django.shortcuts import render
from rest_framework import generics
from accounting.serializers import *
from accounting.models import *

def make_operation(client, oper):
    if oper.act == True:
        client.points = client.points + oper.point
        client.save()
    else:
        if client.points < oper.point:
            raise(ValueError('Not enough points'))
        else:
            client.points = client.points - oper.point
            client.save()


class NewClient (generics.CreateAPIView):
    serializer_class = ClientSerializers

class ClientList (generics.ListAPIView):
    serializer_class = ClientListSerializers
    queryset = Client.objects.all()

class ClientDetail (generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializers
    queryset = Client.objects.all()

class NewOperation (generics.CreateAPIView):
    serializer_class = OperationsSerializers

class OperationsList (generics.ListAPIView):
    serializer_class = OperationsListSerializers
    queryset = Operations.objects.all()

class OperationDetail (generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OperationsSerializers
    queryset = Operations.objects.all()

 