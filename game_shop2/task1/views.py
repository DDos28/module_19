from django.shortcuts import render, redirect
from .forms import UserRegister
from .models import Buyer, Game


def index(request):
    context = {'title': 'Главная страница'}
    return render(request, 'index.html', context)

def game_list(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'game_list.html', context)

def cart(request):
    games = []
    context = {'games': games}
    return render(request, 'cart.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            name = cleaned_data['username']
            age = cleaned_data['age']


            try:
                Buyer.objects.get(name=name)
                return render(request, 'registration_form.html', {'form':form, 'error_message': 'Покупатель с таким именем уже существует'})
            except Buyer.DoesNotExist:
                Buyer.objects.create(name=name, balance=0, age=age)
                return redirect('registration_success')
        else:
            return render(request, 'registration_form.html', {'form': form})
    else:
        form = UserRegister()
        return render(request, 'registration_form.html', {'form': form})


def registration_success(request):
    return render(request, 'registration_success.html')
