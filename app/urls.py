from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name='app'
urlpatterns = [
    path('mycalendar/', login_required(views.MyCalendar.as_view()), name='mycalendar'),
    path(
        'mycalendar/<int:year>/<int:month>/<int:day>/', login_required(views.MyCalendar.as_view()), name='mycalendar'
    ),
    path('detail/<int:pk>/',login_required(views.Detail.as_view()),name='detail'),
    path('update/<int:pk>/',login_required(views.Todoupdate.as_view()),name='update'),
    path('delete/<int:pk>/',login_required(views.Tododelete.as_view()),name='delete'),
]