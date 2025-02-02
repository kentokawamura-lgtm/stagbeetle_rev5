from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Adultmodel
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout,authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


class Todolist(ListView):
    template_name='list.html'
    model = Adultmodel


class applist(ListView):
    template_name='applist.html'
    model = Adultmodel


def Adultlist(request):
    user = request.user
    obj = user.adult.all()
    context = {
        'user':user, 'obj':obj
    }
    return render(request, 'list.html',context)

class Adultcreate(CreateView):
    template_name='create.html'
    model = Adultmodel
    fields = ('name','gender','gener','size','date','memo','image')
    success_url=reverse_lazy('adult:list')
    def form_valid(self, form):
        schedule = form.save(commit=False)
        schedule.user = self.request.user
        schedule.save()
        return redirect('adult:list')



def  Adultdetail(request,pk):
    object = Adultmodel.objects.get(pk=pk)
    return render(request,'adult_detail.html',{'object':object})


class adultupdate(UpdateView):
    template_name='adult_update.html'
    model = Adultmodel
    fields = "__all__"
    success_url = reverse_lazy("adult:list")


class adultdelete(DeleteView):
    template_name='adult_delete.html'
    model = Adultmodel
    fields = "__all__"
    success_url = reverse_lazy("adult:list")

def signup(request):
    if request.method == 'POST':
        username2=request.POST['username']
        password2=request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request,'signup.html',{'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2,'',password2)
            return render(request,'signup.html',{'some':100})
    return render(request,'signup.html',{'some':100})

def login_func(request):
    if request.method == 'POST':
        username2=request.POST['username']
        password2=request.POST['password']
        hoge = authenticate(request, username=username2, password=password2)
        if hoge is not None:
            login(request,hoge)
            return redirect('adult:applist')
        else:
            return redirect('adult:login')
    return render(request,'login.html')

def logout_func(request):
    logout(request)
    return redirect('adult:login') 


def search(request):
    user = request.user
    obj = user.adult.all()
    query = request.GET.get('query')
    if query:
        obj = user.adult.all().filter(name__icontains=query)

    else:
        obj = user.adult.all()
    context = {
        'user':user, 'obj':obj
    }

    return render(request, 'list.html',context)

