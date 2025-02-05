from django.shortcuts import render

def staticImg(request):
    return render(request, 'static_img.html')
