from django.shortcuts import render, redirect

def register(request):
    if request.medthod == 'POST':
        print('submitted reg')
        return redirect('register')
    return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html'),

def dashboard(request):
    return render(request, 'accounts/dashboard.html')