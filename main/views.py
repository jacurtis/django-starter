from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'main/dashboard.html')

def custom_400(request, exception):
    return render(request, 'errors/400.html', status=400)

def custom_401(request, exception):
    return render(request, 'errors/401.html', status=401)

def custom_403(request, exception):
    return render(request, 'errors/403.html', status=403)

def custom_404(request, exception):
    return render(request, 'errors/404.html', status=404)

def custom_500(request):
    return render(request, 'errors/500.html', status=500)