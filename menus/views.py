from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from menus.models import Menu

# Create your views here.
def index(request): 
    context = dict()
    today = datetime.today().date()
    menus = Menu.objects.all()
    context["today"] = today
    context["menus"] = menus
    return render(request, 'menus/index.html', context = context)

def menu_detail(request, pk):
    detail = Menu.objects.get(id=pk)
    return render(request,'menus/detail.html', {'detail':detail})

    