from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "تم التسجيل بنجاح!")
            return redirect('core:home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"مرحباً {user.first_name}!")
                return redirect('core:home')
        else:
            messages.error(request, "الإيميل أو الباسوورد غير صحيح")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "تم تسجيل الخروج بنجاح")
    return redirect('core:home')