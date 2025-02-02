from django.shortcuts import render
import datetime
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.shortcuts import redirect
from django.views import generic
from . import mixins
from .forms import BS4ScheduleForm
from .models import Schedule
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


class MyCalendar(mixins.MonthCalendarMixin, mixins.WeekWithScheduleMixin, generic.CreateView):
    """月間カレンダー、週間カレンダー、スケジュール登録画面のある欲張りビュー"""
    template_name = 'mycalendar.html'
    model = Schedule
    date_field = 'date'
    form_class = BS4ScheduleForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        week_calendar_context = self.get_week_calendar()
        month_calendar_context = self.get_month_calendar()
        context.update(week_calendar_context)
        context.update(month_calendar_context)
        return context



    def form_valid(self, form):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        day = self.kwargs.get('day')
        if month and year and day:
            date = datetime.date(year=int(year), month=int(month), day=int(day))
        else:
            date = datetime.date.today()
        schedule = form.save(commit=False)
        schedule.user = self.request.user
        schedule.date = date
        schedule.save()
        #return render("mycalendar.html",context)
        return redirect('app:mycalendar', year=date.year, month=date.month, day=date.day)


# Create your views here.

class Detail(DetailView):
    template_name='detail.html'
    model=Schedule



class Todoupdate(UpdateView):
    template_name='update.html'
    model = Schedule
    fields = ('summary','description','start_time','end_time','date','priority')
    success_url = reverse_lazy("app:mycalendar")

class Tododelete(DeleteView):
    template_name='delete.html'
    model = Schedule
    fields = ('summary','description','start_time','end_time','date','priority')
    success_url = reverse_lazy("app:mycalendar")