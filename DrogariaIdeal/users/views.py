from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.decorators import user_passes_test

from django.http import HttpResponse

from django.contrib.auth import update_session_auth_hash

import os

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'index.html')


def show_login(request):
    if request.method == "GET":
        return render(request, "userLogin/login.html")
    else:
        context = make_login(request)

        if context.get('is_logged'):
            return HttpResponseRedirect(reverse("users:dashboard"))
        else:
            return render(request, "userLogin/login.html", context)


def make_login(request):
    form = request.POST
    username = form.get('username')
    password = form.get('password')

    user = authenticate(username=username, password=password)
    is_logged = False

    if user is not None:

        login(request, user)
        message = "Logged"

        is_logged = True
    else:
        message = "Incorrect user"

    context = {
        "is_logged": is_logged,
        "message": message,
    }

    return context


@login_required
def logout_view(request, *args, **kwargs):
    
    return logout(request, *args, **kwargs)
