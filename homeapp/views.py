from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect



# Create your views here.
def Homeview(request):
    return render(request,'home.html')

def howto(request):
    return render(request,'howto.html')


class CustomLoginView(LoginView):
    def get_success_url(self):
        return self.request.GET.get('next') or '/home/'