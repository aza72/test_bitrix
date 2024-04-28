from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from personal_account.forms import RegisterUserForm, LoginUserForm, CommentForm
from personal_account.models import User


def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.status = request.POST.get('status')
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return HttpResponseRedirect('login')
    else:
        form = RegisterUserForm()
    return form

class Accounts(CreateView):
    form_class = RegisterUserForm
    template_name = 'personal_account/base.html'



def log(request):
    return render(request,"personal_account/login.html")


def autorize(request):
    return render(request,"personal_account/autorize.html")

def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect('auth')
    else:
        form = LoginUserForm()
    return form


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/account')

@login_required(login_url='acc')
def personal_account(request):
    return render(request, "personal_account/personal_account.html")

@login_required(login_url='acc')
def personal_account1(request):
    return render(request, "personal_account/personal_account1.html")

def customers(request):
    customers = User.objects.filter(status='Заказчик')
    return render(request, "personal_account/customers.html",{'customers':customers})

def executor(request):
    executor = User.objects.filter(status='Исполнитель')
    return render(request, "personal_account/executor.html",{'executor':executor})

def comment(request):
    form = CommentForm()
    return render(request, "personal_account/comment.html", {'form': form})



