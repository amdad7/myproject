from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.views import generic
from .models import *
from django.urls import reverse
from .forms import userform
from django.utils import timezone
# Create your views here.
"""login system"""


def indexv(request):
    return render(request,'datac/index.html',{'errcode':1})
def login(request):
    try:
        m=User.objects.get(user_text=request.POST['username'])
        if m.password == request.POST['password']:
            request.session[str(m.id)]=m.id
            return HttpResponseRedirect('/datac/'+str(m.id)+'/')
        else:
            return render(request,'datac/index.html',{'errcode':0,
            'err':"wrong password"})

    except:
        return render(request,'datac/index.html',{'errcode':0,
        'err':"wrong username"})
def home(request,id):
    user=get_object_or_404(User,pk=id)
    try:
        if request.session[str(id)]==user.id:
            return render(request,'datac/home.html',{'user':user})
        else:
            return HttpResponseRedirect(reverse('datac:index'))
    except:
        return HttpResponseRedirect(reverse('datac:index'))
def logout(request,id):
    del request.session[str(id)]
    return render(request,'datac/index.html',{'errcode':1})
def Create_user(request):
    return render(request,'datac/create.html',{'form':userform,'error_code':0})

def create(request):
    if request.method == 'POST':
        form=userform(request.POST)
        if form.is_valid():
            try:
                User.objects.get(user_text=form.cleaned_data['user_name'])
                return render(request,'datac/create.html',{'form':userform,'error_code':1})
            except:
                User.objects.create(user_text=form.cleaned_data['user_name'],
                    password=form.cleaned_data['password'],
                    pub_date=timezone.now())
                return render(request,'datac/index.html',{'errcode':1})

        else:
            return render(request,'datac/index.html',{'errcode':0,
            'err':'invalid entry'})
    else:
        return render(request,'datac/index.html',{'errcode':0,
        'err':'request error'})

"""login system end"""
