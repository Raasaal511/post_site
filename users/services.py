from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render

from .forms import UserCreateForm, UserLoginForm


def user_register(request):
    form = UserCreateForm()

    if request.user.is_authenticated:
        return redirect('users:profile')

    if request.method == 'POST':
        form = UserCreateForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    return render(request, 'account/register.html', {'form': form})


def user_login(request):
    form = UserLoginForm()

    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

    return render(request, 'account/login.html', {'form': form})
