from django.shortcuts import render

# Create your views here.
from .models import City, Coach, Place, Sportclub, Category, Level, Fencer, Competition, Result

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    #Количество посещений страницы.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(
        request,
        'index.html',
        context={'num_visits':num_visits},
  )

def coaches(request):
    """
    Функция отображения для страницы с тренерами.
    """
    return render(
        request,
        'coaches.html',
  )

def awards(request):
    """
    Функция отображения для страницы с фото.
    """
    return render(
        request,
        'awards.html',
  )

def rasp60(request):
    """
    Функция отображения для расписания зала на ул.60 лет.
    """
    return render(
        request,
        'rasp60.html',
  )

def raspM(request):
    """
    Функция отображения для расписания зала на ул.Малаховской.
    """
    return render(
        request,
        'raspM.html',
  )

def raspES(request):
    """
    Функция отображения для расписания зала на ул.Елены Стасовой.
    """
    return render(
        request,
        'raspES.html',
  )


from django.views import generic

class FencerListView(generic.ListView):
    model = Fencer
    paginate_by = 10

class FencerDetailView(generic.DetailView):
    model = Fencer

class CompetitionListView(generic.ListView):
    model = Competition
    paginate_by = 10

class CompetitionDetailView(generic.DetailView):
    model = Competition

class ResultListView(generic.ListView):
    model = Result

    def get_queryset(self):
        return Result.objects.order_by("result")