from django.shortcuts import render, get_object_or_404, redirect
from .models import Design, User, CommentLike
from .forms import DesignSearchForm
from django.views.generic import TemplateView, ListView
from django.db.models import Q

# Create your views here.
def index(request):
    design = Design.objects.all()[:8]
    ava = User.objects.all()
    return render(request, 'index.html', {'design':design}, {'ava':ava})

def formPublish(request):
    return render(request,'form-publish.html')

def profile(request):
    return render(request, 'profile.html')

def user(request):
    return render(request, 'user.html')

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

def design(request):
    searchvalue=''
    form= DesignSearchForm(request.POST or None)
    if form.is_valid():
        searchvalue= form.cleaned_data.get("search")
    searchresults= Design.objects.filter(
        Q(title__icontains= searchvalue) | Q(description__icontains= searchvalue)
        )
    context= {'form': form,
              'searchresults': searchresults,
              }
    return render(request, 'design.html', context)

class SearchResultsView(ListView):
    model = Design
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Design.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(tags__icontains=query)
        )
        return object_list

def detail(request, id):
    detail = get_object_or_404(Design, pk=id)
    user = get_object_or_404(User, pk=1)
    
    return render(request, 'picture-detail.html', {'detail':detail})
