from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Projects, Resume
from .forms import ProjectsModelForm, ResumeModelForm
from django.core.paginator import Paginator


# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def projects(request):
    qs = Projects.objects.all()
    page = request.GET.get('page', '1')
    paginator = Paginator(qs, '2')
    paginated_qs = paginator.get_page(page)
    return render(request, 'projects.html',{'paginated_qs': paginated_qs})

def resume(request):
    qs = Resume.objects.all()
    page = request.GET.get('page', '1')
    paginator = Paginator(qs, '2')
    paginated_qs = paginator.get_page(page)
    return render(request, 'Resume.html',{'paginated_list': paginated_qs})
    
def resume_detail(request, pk):
    
    resume = get_object_or_404(Resume, pk=pk)
    return render(request, 'resume_detail.html', {'resume':resume})

def projects_detail(request, pk):
    qs = Projects.objects
    page = request.GET.get('page', '1')
    paginator = Paginator(qs, '2')
    paginated_qs = paginator.get_page(page)
    projects = get_object_or_404(Resume, pk=pk)
    return render(request, 'projects_detail.html', {'projects':projects}, {'paginated_list' : paginated_qs})
    


@login_required
def projects_create(request):
    if request.method == 'POST':
        form = ProjectsModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ProjectsModelForm()
    return render(request, 'projects_create.html', {'form':form})

@login_required
def resume_create(request):
    if request.method == 'POST':
        form = ResumeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ResumeModelForm()
    return render(request, 'resume_create.html', {'form':form})

def contact(request):
    if(request.method == 'POST'):
        item = Profile()
        item.name = request.POST['name']
        item.email = request.POST['email']
        item.phone = request.POST['phone']
        item.message = request.POST['message']
        item.save()
        context ={
            
            'name' : request.POST['name'],
            'email' : request.POST['email'],
            'phone' : request.POST['phone'],
            'message': request.POST['message'],

        }
        
        redirect('contactor.html', context)
    #과연 이 form을 유지 가능한가?
    return render(request, 'contact.html')
    


def contactor(request):
    if request.method == 'POST':
        item = get_object_or_404(Profile, name=request.POST['name'])
        item.name = request.POST['name']
        item.email = request.POST['email']
        item.phone = request.POST['phone']
        item.message = request.POST['message']
        item.save()
        context = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'message': request.POST['message'],
        }
        return render(request, 'contactor.html', context)
    return render(request, 'contactor.html')

