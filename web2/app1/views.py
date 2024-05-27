from django.shortcuts import render, redirect
from app1 import models
from django.forms import ModelForm
# Create your views here.
from django.http import HttpResponse


class MyForm(ModelForm):
    class Meta:
        model = models.message
        fields = ["mes1", "mes2", "mes3", "mes4"]

def index(request):
    if request.method == "GET":
        form = MyForm()
        return render(request, 'index.html',{"form":form})
