from django.shortcuts import render, HttpResponseRedirect
from App_Login.forms import SignUp, LogIn, EditProfile
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from App_Login.models import UserProfile
from django.contrib.auth.decorators import login_required

def sign_up(request):
    form =  SignUp()
    registered = False
    if request.method == 'POST':
        form = SignUp(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('App_Login:login'))
    return render(request, 'App_Login/sign_up.html', context={'title':'Sign up . Facebook', 'form':form})

def login_page(request):
    form = LogIn()
    if request.method == 'POST':
        form = LogIn(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Post:home'))
    return render(request, 'App_Login/login.html', context={'title':login, 'form':form})

@login_required
def profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)
    return render(request, 'App_Login/profile.html', context={'title':'Profile','form':form, })

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))