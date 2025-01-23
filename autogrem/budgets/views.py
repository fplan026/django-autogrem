from django.shortcuts import render
from django.http import HttpResponse
from .models import Budget

def home(request):
    budgets = Budget.objects.all()
    return render(request, 'home.html', {'budgets': budgets})
