from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd


def get_town_index():
    with open('TOWN_INDEX.geojson', 'r') as f:
        towns = f.read();
    return towns

# Create your views here.
def index(request):
    context = {
            'name':'user', 
            'towns':get_town_index()
    }

    return render(request, 'main/index.html', {'data':context})
