from django.urls import path,include
from . import views
from django.contrib.auth.decorators import login_required

app_name='child'
urlpatterns = [
    path('list/',login_required(views.Childlist),name='child_list'),
    path('create/',login_required(views.Childcreate.as_view()),name='child_create'),
    path('detail/<int:pk>/',login_required(views.Childdetail),name='child_detail'),
    path('update/<int:pk>/',login_required(views.Childupdate.as_view()),name='child_update'),
    path('delete/<int:pk>/',login_required(views.Childdelete.as_view()),name='child_delete'),
    path('signup/',views.signup,name='child_signup'),
    path('login/',views.login_func,name='child_login'),
    path('logout/',views.logout_func,name='child_logout'),
    path('search/',views.search,name='child_search'),
]
