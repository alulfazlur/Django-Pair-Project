from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'homeactive':True})

def formPublish(request):
    return render(request,'form-publish.html')

def PictureDetail(request):
    return render(request,'picture-detail.html')