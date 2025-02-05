from django.shortcuts import render,redirect
from .models import CourseData,Feedback
def HomePage(request):
    return render(request,'home.html')
def ContactPage(request):
    return render(request,'contact.html')
def ServicePage(request):
    data=CourseData.objects.all()
    return render(request,'service.html',{'data':data})
def FeedbackPage(request):
    if request.method=='GET':
        data1= Feedback.objects.all()
        return render(request,'feedback.html',{'data1':data1})
    else:
        Feedback(
            feedback_data = request.POST.get('feedback')
        ).save()
        return redirect(FeedbackPage) 

def GalleryPage(request):
    return render(request,'gallery.html')