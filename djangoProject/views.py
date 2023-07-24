from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LogoutView
from django.urls import reverse
from .models import Inspection, Condition


class MyLogoutView(LogoutView):
    next_page = 'login'


def login_view(request, reason=None):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})

    return render(request, 'login.html')


@login_required
def home_view(request):
    inspections = Inspection.objects.all()
    return render(request, 'home.html', {'username': request.user.username, 'inspections': inspections})


@login_required
def redirected_view(request, inspection_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    inspection = get_object_or_404(Inspection, pk=inspection_id)
    conditions = Condition.objects.filter(Inspection_id=inspection_id)

    return render(request, 'redirect.html', {
        'username': request.user.username,
        'inspection': inspection,
        'conditions': conditions,
    })