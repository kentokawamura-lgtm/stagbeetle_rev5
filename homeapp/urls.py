from django.urls import path
from . import views
app_name='home'
urlpatterns = [
    path('',views.Homeview,name='home'),
    path('howto/',views.howto,name='howto'),
]