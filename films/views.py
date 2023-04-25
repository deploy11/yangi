from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.views.generic import DetailView
# Create your views here.
def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        film = Film.objects.filter(Q(title__icontains=q)).order_by('-id') 
        category = Category.objects.all()
    else:
        category = Category.objects.all()
        film = Film.objects.all().order_by('-id')
      
    return render(request,'list.html',{'film':film,'category':category,})

class detail(DetailView):
    model = Film
    template_name = 'detail.html'

def categores(request):
    qi = request.GET.get('category')
    category = Category.objects.all()
    film = Film.objects.all()
    if category == None:
            film = Film.objects.all()
    else:
            film = Film.objects.filter(category__nomi=qi)
    return render(request,'cate.html',{'film':film,'category':category,'qi':qi})
