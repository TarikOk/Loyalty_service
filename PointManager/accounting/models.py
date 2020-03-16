from django.db import models
from django.shortcuts import render
from rest_framework import generics

class Client(models.Model):
    id = models.CharField(verbose_name='Id', primary_key=True, max_length=50)
    name = models.CharField(verbose_name='Name',max_length=50)
    points = models.IntegerField(verbose_name='Points')

    def __str__ (self):
        return f'{self.id} {self.name}'

class Operations(models.Model):
    client = models.ForeignKey(Client, verbose_name='client', on_delete = models.CASCADE)
    descript = models.CharField(verbose_name='Descript',max_length=100)
    act = models.BooleanField(verbose_name='Act')
    point = models.IntegerField(verbose_name='Point')
    date = models.DateTimeField(auto_now_add=True)