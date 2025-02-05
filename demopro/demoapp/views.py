from django.shortcuts import render
from .models import Demo
# Create your views here.
def demo(request):
    return render(request,"hello.html")