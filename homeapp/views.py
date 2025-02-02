from django.shortcuts import render

# Create your views here.
def Homeview(request):
    return render(request,'home.html')

def howto(request):
    return render(request,'howto.html')