from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .forms import signform
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# --------------------------------------------------------------------------------------------------------------------------------------


def signin(request):
    if request.method == 'POST':
        form = signform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index') 
            else:
                messages.error(request, 'Invalid email or password')
    else:
        form = signform()

    return render(request, 'signin.html', {'form': form})

from .forms import registerform  

def register(request):
    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 == password2:

                user = User.objects.create_user(username=email, email=email, password=password1)
                user.first_name = first_name
                user.last_name = last_name
                user.save()

                messages.success(request, f'Account created for {first_name} {last_name}')
                return redirect('signin')
            else:
                messages.error(request, 'passwords do not match')

    form = registerform()
    return render(request, 'register.html', {'form':form})

# ------------------------------------------------------------------------------------------------------------------------------------------
@login_required
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
# ------------------------------------------------------------------------------------------------------------------------------------------
@login_required
def about(request):
    template = loader.get_template('aboutus.html')
    return HttpResponse(template.render())
# ------------------------------------------------------------------------------------------------------------------------------------------
@login_required
def feature(request):
    template = loader.get_template('features.html')
    return HttpResponse(template.render())
# ------------------------------------------------------------------------------------------------------------------------------------------
from .models import contactdetail
from .forms import contactform
@login_required
def contact(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
                form.save()
                return redirect('contacts')
        
    else:
        form=contactform()

    return render(request,'contact.html',{'form':form})

def contacts(request):
    det=contactdetail.objects.all()
    return render(request,'index.html',{'det':det})

# ----------------------------------------------------------------------------------------------------------------------------------------------
@login_required
def account(request):
    return render(request, 'Account.html', {'user':request.user})
# ----------------------------------------------------------------------------------------------------------------------------------------------

def custom_logout(request):
    logout(request)
    return redirect('signin')

# ---------------------------------------------------------------------------------------------------------------------------------------------- 