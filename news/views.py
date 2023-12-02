from django.shortcuts import render
from .models import State
from django.views.generic import DetailView


def index(request):
    context = {'title': 'Главная',
               'carusel': State.objects.all()[:4],
               'main': State.objects.all()[4],
               'break': State.objects.all()[5:7],
               'dm': State.objects.all()[7:10],
               'today_most_popular': State.objects.all()[10:12]
               }
    return render(request, 'news/index.html', context)


class NewDetailView(DetailView):
    model = State
    template_name = 'news/single_post.html'
    context_object_name = 'state'


def contact(request):
    context = {'title': 'Контакты'}
    return render(request, 'news/contact.html', context)
