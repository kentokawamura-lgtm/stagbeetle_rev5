from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
app_name = 'kakeibo'

urlpatterns = [
    path('', login_required(views.PaymentList.as_view()), name='payment_list'),
    path('income_list/', login_required(views.IncomeList.as_view()), name='income_list'),
    path('payment_create/', login_required(views.PaymentCreate.as_view()), name='payment_create'),
    path('income_create/', login_required(views.IncomeCreate.as_view()), name='income_create'),
    path('payment_delete/<int:pk>/', login_required(views.PaymentDelete.as_view()), name='payment_delete'),
    path('income_delete/<int:pk>/', login_required(views.IncomeDelete.as_view()), name='income_delete'),
    path('monthly_balance/<int:year>/<int:month>/', login_required(views.MonthlyBalance.as_view()), name='monthly_balance'),
    path('balance_transition/', login_required(views.TransitionView.as_view()), name='balance_transition'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_func,name='login'),
    path('logout/',views.logout_func,name='logout'),
]
