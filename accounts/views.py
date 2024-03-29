from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from user_contacts.models import UserContact


def register(request):
    if request.method == 'POST':
    # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
                return redirect('register')
            else:
                # Check email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already registered')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password
                    )
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'Your are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are now registered')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    return render(request, 'accounts/register.html')

def user_login(request):
    if request.method == 'POST':
        # Login user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged ou t')
        return redirect('index')
    return render(request, 'accounts/logout.html'),

def dashboard(request):
    user_id = request.user.id
    user_contacts = UserContact.objects.filter(user_id=user_id)

    context = {
        'user_contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)