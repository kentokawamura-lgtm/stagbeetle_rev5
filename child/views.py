from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Childmodel
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout,authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from adult.models import Adultmodel



# Create your views here.


def Childlist(request):
    user = request.user
    obj = user.child.all()
    obj2 = user.adult.all()
    context = {
        'user':user, 'obj':obj, 'obj2':obj2
    }
#種親情報を取得


    return render(request, 'child_list.html',context)

class Childcreate(CreateView):
    template_name='child_create.html'
    model = Childmodel
    fields = ('number', 'name','size_ad','ad_date', 'gender','gener','date','date_1','date_2','date_3','date_4','weight_1','weight_2','weight_3','weight_4','memo')
    success_url=reverse_lazy('child:child_list')
    def form_valid(self, form):
        schedule = form.save(commit=False)
        schedule.user = self.request.user
        schedule.save()
        return redirect('child:child_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # フォーム送信後、前回入力されたデータを保持する
        if self.request.method == 'POST' and self.request.POST:
            # POSTデータが送信されていれば、それをフォームに渡す
            context['form'].initial = self.request.POST
        
        return context




def  Childdetail(request,pk):
    object = Childmodel.objects.get(pk=pk)
    return render(request,'child_detail.html',{'object':object})


class Childupdate(UpdateView):
    template_name='child_update.html'
    model = Childmodel
    fields =  ('number', 'name','size_ad','ad_date', 'gender','gener','date','date_1','date_2','date_3','date_4','weight_1','weight_2','weight_3','weight_4','memo')
    success_url = reverse_lazy("child:child_list")


class Childdelete(DeleteView):
    template_name='child_delete.html'
    model = Childmodel
    fields =  ('number', 'name','size_ad','ad_date', 'gender','gener','date','date_1','date_2','date_3','date_4','weight_1','weight_2','weight_3','weight_4','memo')
    success_url = reverse_lazy("child:child_list")

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
            return redirect('child:child_login')
    return render(request,'child_login.html')

def logout_func(request):
    logout(request)
    return redirect('child:child_login') 


def search(request):
    user = request.user
    obj = user.child.all()
    query = request.GET.get('query1')
    if query:
        obj = user.child.all().filter(name__icontains=query)
        obj = user.child.all().filter(date__icontains=query)
    else:
        obj = user.child.all()
    context = {
        'user':user, 'obj':obj
    }

    return render(request, 'child_list.html',context)