from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile



# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'projects.html')

def resume(request):
    return render(request, 'resume.html')



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
    if(request.method == 'POST'):
        item = Profile().objects.filter(name=item.name)
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
    return render(request, 'contactor.html')
        