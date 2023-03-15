from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import CustomUser
from .forms import LoginForm, RegistrationForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = CustomUser.objects.get(email=email)
                if check_password(password, user.password):
                    request.session['user_id'] = user.id
                    return redirect('home")
            except:
                return KeyError

