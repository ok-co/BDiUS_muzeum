from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard
        else:
            return render(request, 'staff/login.html', {'error': 'Błędy login lub hasło'})
    return render(request, 'staff/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

@login_required
def dashboard_view(request):
    return render(request, 'staff/dashboard.html')
