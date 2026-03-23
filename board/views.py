from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from datetime import date

def index(request):
    today = date.today()
    return render(request, 'board/index.html', {'today' : today})