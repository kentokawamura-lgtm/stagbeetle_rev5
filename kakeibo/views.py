import datetime
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Payment, Income
from .forms import PaymentSearchForm, IncomeSearchForm, \
    PaymentCreateForm, IncomeCreateForm,\
    TransitionGraphSearchForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from kakeibo import plugins
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout,authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models import Sum




class PaymentList(LoginRequiredMixin,generic.ListView):
    """支出一覧ページ"""
    template_name = 'payment_list.html'
    model = Payment
    ordering = '-date'
    paginate_by = 10
    
    def get_queryset(self):
        
        queryset = super().get_queryset().filter(user=self.request.user)
        
        self.form = form = PaymentSearchForm(self.request.GET or None)
        
        if form.is_valid():
            year = form.cleaned_data.get('year')
            # yearとmonthにつき何も選択されていないときは0の文字列が入るため、除外
            # forms.pyを参照
            if year and year != '0':
                queryset = queryset.filter(date__year=year)

            month = form.cleaned_data.get('month')
            if month and month != '0':
                queryset = queryset.filter(date__month=month)

            greater_than = form.cleaned_data.get('greater_than')
            if greater_than:
                queryset = queryset.filter(amount__gte=greater_than)

            less_than = form.cleaned_data.get('less_than')
            if less_than:
                queryset = queryset.filter(amount__lte=less_than)

            key_word = form.cleaned_data.get('key_word')
            if key_word:
                # 空白で区切られていた場合は分割して繰り返す、and検索
                for word in key_word.split():
                    queryset = queryset.filter(description__icontains=word)

            category = form.cleaned_data.get('search_category')
            if category:
                queryset = queryset.filter(category=category)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form
        context['create_form'] = PaymentCreateForm
        context['action_url'] = '/payment_create/'
        
        return context


class IncomeList(generic.ListView):
    """収入一覧ページ"""
    
    template_name = 'income_list.html'
    model = Income
    ordering = '-date'
    paginate_by = 10
    
    def get_queryset(self):
        self.form = form = IncomeSearchForm(self.request.GET or None)
        queryset = super().get_queryset().filter(user=self.request.user)

        if form.is_valid():
            year = form.cleaned_data.get('year')
            if year and year != '0':
                queryset = queryset.filter(date__year=year)

            month = form.cleaned_data.get('month')
            if month and month != '0':
                queryset = queryset.filter(date__month=month)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = IncomeSearchForm(self.request.GET or None)
        context['create_form'] = IncomeCreateForm
        context['action_url'] = '/income_create/'
        
        return context





class PaymentCreate(LoginRequiredMixin, generic.CreateView):
    """支出登録"""
    model = Payment
    template_name = 'payment_create.html'  # テンプレート名を指定
    fields= ('date','category','amount','description')
    def get_success_url(self):
        return reverse_lazy('kakeibo:payment_list')

    def form_valid(self, form):
        """フォームが有効な場合、支出を保存し、現在のユーザーを設定"""
        self.object = form.save(commit=False)  # まだ保存しない
        self.object.user = self.request.user  # 現在ログインしているユーザーを設定
        self.object.save()  # 保存
        
        # モーダルウィンドウを閉じてリダイレクト
        return redirect('kakeibo:payment_list')


class IncomeCreate(generic.CreateView):
    """支出登録"""
    model = Income
    template_name = 'income_create.html'  # テンプレート名を指定
    fields= ('date','category','amount','description')
    def get_success_url(self):
        return reverse_lazy('kakeibo:income_list')

    def form_valid(self, form):
        """フォームが有効な場合、支出を保存し、現在のユーザーを設定"""
        self.object = form.save(commit=False)  # まだ保存しない
        self.object.user = self.request.user  # 現在ログインしているユーザーを設定
        self.object.save()  # 保存
        
        # モーダルウィンドウを閉じてリダイレクト
        return redirect('kakeibo:income_list')





class PaymentDelete(generic.DeleteView):
    """支出削除"""
    model = Payment

    def get_success_url(self):
        return reverse_lazy('kakeibo:payment_list')

    def delete(self, request, *args, **kwargs):
        self.object = payment = self.get_object()

        payment.delete()
        msg = plugins.success_message_for_item('Delete',
                                               'Payment',
                                               payment.date,
                                               payment.category,
                                               payment.amount)
        messages.info(self.request, msg)
        return redirect(self.get_success_url())


class IncomeDelete(generic.DeleteView):
    """収入削除"""
    model = Income

    def get_success_url(self):
        return reverse_lazy('kakeibo:income_list')

    def delete(self, request, *args, **kwargs):
        self.object = income = self.get_object()
        income.delete()
        msg = plugins.success_message_for_item('Delete',
                                               'Income',
                                               income.date,
                                               income.category,
                                               income.amount)
        messages.info(self.request, msg)
        return redirect(self.get_success_url())





class MonthlyBalance(plugins.MonthlyBalanceMixin, generic.TemplateView):
    """月間収支ページ"""
    template_name = 'monthly_balance.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        print(user)


        data = self.get_monthly_balance_data()
        context.update(data)

        return context


class TransitionView(plugins.BalanceTransitionMixin, generic.TemplateView):
    """月毎の収支推移ページ"""
    template_name = 'balance_transition.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.form = form = TransitionGraphSearchForm(self.request.GET or None)
        context['search_form'] = self.form

        data = self.get_balance_transition_data(form)
        context.update(data)

        return context


def signup(request):
    if request.method == 'POST':
        username2=request.POST['username']
        password2=request.POST['password']
        
        try:
            get_user_model().objects.get(username=username2)
            return render(request,'signup.html',{'error':'このユーザーは登録されています'})
        except:
            user = get_user_model().objects.create_user(username2,'',password2)
            return render(request,'signup.html',{'some':100})
    return render(request,'signup.html',{'some':100})

def login_func(request):
    if request.method == 'POST':
        username2=request.POST['username']
        password2=request.POST['password']
        hoge = authenticate(request, username=username2, password=password2)
        if hoge is not None:
            login(request,hoge)
            return redirect('kakeibo:payment_list')
        else:
            return redirect('kakeibo:login')
    return render(request,'login.html')

def logout_func(request):
    logout(request)
    return redirect('kakeibo:login') 
