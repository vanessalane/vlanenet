from django.shortcuts import render

def HomePageView(request):
    return render(request, 'home.html')

def ResumeView(request):
    return render(request, 'resume.html')
