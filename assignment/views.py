
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User, auth
from .decorators import allowed_users
from django.contrib.auth.models import Group
from .models import *
from django.http import JsonResponse
import bcrypt
# Create your views here.


def index(request):
    return render(request, 'index.html')

def name(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('Logged in ')
            return redirect('/product')
        else:
            print('You are Not logged in')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():

            username=form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            user=User.objects.create_user(username=username, email=email, password=password1)
            group=Group.objects.get(name='customer')
            user.groups.add(group)
            user.save()
            messages.success(request, 'Account was Created for:' + username)
            return redirect('/login')
            print("Pradipc")
    form = CreateUserForm()


    context = {'form': form}

    return render(request, 'register.html', context)

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
def dashboard(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'cdashboard.html', context)

@login_required(login_url='/login')
@allowed_users(allowed_roles=['customer'])
def product(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'cdashboard.html', context)




def exit(request):
    auth.logout(request)
    return redirect('/login')

def shop(request):
    products = Product.objects.all()
    if request.method=='POST':
        cardholdername = request.POST['name']
        number = request.POST['card_number']
        bytes = number.encode('utf-8')
        salt = bcrypt.gensalt()
        cardnumber = bcrypt.hashpw(bytes, salt)
        cpsv = request.POST['cvv']
        bytes = cpsv.encode('utf-8')
        falt = bcrypt.gensalt()
        csv = bcrypt.hashpw(bytes, falt)
        cardtype = request.POST['card_type']
        cardexpiry = request.POST['exp_date']
        formdetain = order(cardholdername=cardholdername, cardnumber=cardnumber, cardtype=cardtype,
                           cardexpiry=cardexpiry, csv=csv)
        formdetain.save()

    context = {'products': products}
    return  render(request, 'shop.html', context)
def insecure(request):

    return render (request, 'insecure.html')

def verifyotp(request):
    return render(request, 'verify.html')


def apiOverView(request):
    return JsonResponse("API BASE POINT", Safe=False)

