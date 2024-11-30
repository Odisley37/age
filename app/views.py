import json
from django.shortcuts import render
from ai.models import AIResult
from . import metrics



def home(request):
    

    return render(request, 'home.html')