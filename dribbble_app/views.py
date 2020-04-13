from django.shortcuts import render, get_object_or_404, redirect
from .models import Design, User, CommentLike
from .forms import DesignSearchForm
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render

from django.http import HttpResponseRedirect
from .forms import UploadFileForm

# Create your views here.
# def index(request):
    # design = Design.objects.all()[:4]
    # return render(request, 'index.html', {'design':design})

def formPublish(request):
    return render(request,'form-publish.html')

def profile(request):
    return render(request, 'profile.html')

def user(request):
    return render(request, 'user.html')

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
            Q(fullname__fullname__icontains=query) | 
            Q(title__icontains=query) | 
            Q(description__icontains=query) | 
            Q(tags__icontains=query)
        )
        return object_list


def detail(request, id):
    designs = get_object_or_404(Design, pk=id)
    user = get_object_or_404(User, pk=1)
    ava = get_object_or_404(User, fullname=designs.fullname)
    
    
    if request.method == 'POST':
        cm = CommentLike.objects.create(
            name = "anonymous",
            design = Design.objects.get(pk=id),
            comment = request.POST.get('tulis-komen'),
        )
        cm.save()        
    
    obj = CommentLike.objects.first()
    field_value = getattr(obj, 'design')
    count = CommentLike.objects.filter(design=field_value).count()
    
    return render(request,'picture-detail.html', {
        'post_active':True, 'designs':designs, 'count':count, 'ava':ava})
    
def designLike(request, id):
    details = get_object_or_404(Design, pk=id)
    dL = details.like
    Design.objects.filter(pk=id).update(like=dL+1)
    return redirect('/'+str(id)+'/')

def index(request):
    design_list = Design.objects.all().order_by('-id')
    paginator = Paginator(design_list, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})










# Imaginary function to handle an uploaded file.
from somewhere import handle_uploaded_file

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)