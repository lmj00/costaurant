from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import time
from time import localtime, strftime
from django.utils import timezone

# Create your views here.
def index(request): 
    today = datetime.today().date()
    context = {"date" : today}
    return render(request, 'menus/index.html', context = context)