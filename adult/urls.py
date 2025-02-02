from django.urls import path,include
from . import views
from django.contrib.auth.decorators import login_required

app_name='adult'
urlpatterns = [
    path('list/',login_required(views.Adultlist),name='list'),
    path('create/',login_required(views.Adultcreate.as_view()),name='create'),
    path('detail/<int:pk>/',login_required(views.Adultdetail),name='adult_detail'),
    path('update/<int:pk>/',login_required(views.adultupdate.as_view()),name='adult_update'),
    path('delete/<int:pk>/',login_required(views.adultdelete.as_view()),name='adult_delete'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_func,name='login'),
    path('logout/',views.logout_func,name='logout'),
    path('applist/',views.applist.as_view(),name='applist'),
    path('search/',views.search,name='search'),
]