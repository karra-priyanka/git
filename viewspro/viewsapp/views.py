from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    text='welcome to Data Pulse Institute'
    return HttpResponse(text)