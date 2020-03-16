from django.contrib.auth.models import User, Group
from rest_framework import serializers
from accounting.models import *


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ClientListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class OperationsSerializers (serializers.ModelSerializer):
    class Meta:
        model = Operations
        fields = ('client', 'descript', 'act', 'point')
        
class OperationsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Operations
        fields = ('client', 'descript', 'act', 'point','date')

        