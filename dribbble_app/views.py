from django.shortcuts import render
from .models import CommentLike, UserDesign

# Create your views here.
def index(request):
    return render(request, 'index.html', {'homeactive':True})

def formPublish(request):
    return render(request,'form-publish.html')

def PictureDetail(request):
    # pict_detail = CommentLike.objects.all()
    # desain = UserDesign.objects.all()
    comment = CommentLike.objects.all()
    
    return render(request,'picture-detail.html', 
                #   {"design":desain}
                  {'comment':comment})

def PictureDetail(request): 
    if request.method == 'POST':
        cm = CommentLike.objects.create(
            name = "anonymous",
            comment = request.POST.get('tulis-komen')
        )
        cm.save()        
        
    comment = CommentLike.objects.all()
    return render(request,'picture-detail.html', {
        'comment':comment,
        'post_active':True})
