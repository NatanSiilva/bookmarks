from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm


def User_login(request):

    http_referer = request.META.get(
        'HTTP_REFERER', reverse('login'))

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # messages.error(request, 'Authenticated successfully')
                    return HttpResponse('Authenticated successfully')
                else:
                    messages.error(request, 'Disabled account')
                    return redirect(http_referer)
            else:
                messages.error(request, 'Invalid login')
                return redirect(http_referer)
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def Dashboard(request):
    return render(request, 'account/dashboard.html', {'section':'dashboard'})