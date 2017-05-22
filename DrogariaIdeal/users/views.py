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
    return render(request, 'userLogin/dashboard.html')


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



@login_required
@user_passes_test(lambda user: user.is_staff, login_url='/accounts/dashboard/')
def register(request):

    if request.method == "GET":
        return render(request, 'userRegister/register.html')
    else:
        form = request.POST
        first_name = form.get('first_name')
        last_name = form.get('last_name')
        password = form.get('password')
        confirmPassword = form.get('confirmPassword')
        email = form.get('email')
        user_type = form.get('user_type')

        resultCheck = fullValidationRegister(form)
        resultCheck += fullValidation(form)

        if len(resultCheck) != 0:
            return render(
                request,
                'userRegister/register.html',
                {'falha': resultCheck})

        try:
            if user_type == 'common':
                user = User.objects.create_user(first_name=first_name,
                                                last_name=last_name,
                                                password=password,
                                                username=email)
            else:
                user = User.objects.create_superuser(first_name=first_name,
                                                     last_name=last_name,
                                                     password=password,
                                                     username=first_name,
                                                     email=email)

        except IntegrityError as e:
            return render(request, 'userRegister/register.html',
                          {'falha': 'Invalid email, email already exist'})
        except:
            return render(request, 'userRegister/register.html',
                          {'falha': 'unexpected error'})

        user.save()
        messages.success(request, 'Usuario registrado com sucesso')

    return render(request, 'userLogin/dashboard.html')

def fullValidation(form):
    first_name = form.get('first_name')
    last_name = form.get('last_name')
    email = form.get('email')
    original_email = form.get('original_email')

    resultCheck = ''
    resultCheck += check_name(first_name, last_name)
    resultCheck += check_email(email)
    resultCheck += check_email_exist(email, original_email)

    return resultCheck


def fullValidationRegister(form, user=None):
    currentPassword = form.get('currentPassword')
    password = form.get('password')
    confirmPassword = form.get('confirmPassword')

    resultCheck = ''
    if user is not None:
        resultCheck += check_current_password(user, currentPassword)
        resultCheck += check_password_lenght(password, confirmPassword)
        resultCheck += check_password(password, confirmPassword)

    return resultCheck

def check_name(first_name, last_name):
    if not first_name.isalpha() or not last_name.isalpha():
        return 'Nome deve conter apenas letras'
    else:
        return ''


def check_email(email):
    if '@' not in email or '.' not in email or ' ' in email:
        return 'Email invalido'
    else:
        return ''


def check_email_exist(email, original_email):
    if User.objects.filter(email=email).exists() and email != original_email:
        return ' -- E-mail ja esta cadastrado no nosso banco de dados'
    else:
        return ''


def check_password_lenght(password, confirmPassword):
    if len(password) < 6 and password != confirmPassword:
        return ' -- Senha Invalida, digite uma senha com no minimo 6 letras'
    else:
        return ''


def check_password(password, confirmPassword):
    if password != confirmPassword:
        return ' -- Senha invalida! Senhas de cadastros diferentes'
    else:
        return ''


def check_current_password(user, currentPassword):

    if not user.check_password(currentPassword):
        return ' -- Campo de Senha atual diferente da Senha Atual!'
    else:
        return ''
