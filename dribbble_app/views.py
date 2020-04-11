from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'homeactive':True})

def formPublish(request):
    return render(request,'form-publish.html')

def profile(request):
    return render(request, 'profile.html', {'homeactive':True})

def user(request):
    return render(request, 'user.html', {'homeactive':True})