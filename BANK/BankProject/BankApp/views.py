from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    program = Programming.objects.all()
    d = {'program': program}
    return render(request,'index.html',d)

def load_courses(request):
    programming_id = request.GET.get('programming')
    courses = Course.objects.filter(programming_id=programming_id).order_by('name')
    return render(request, 'courses_dropdown_list_options.html', {'courses': courses})

def home(request):
    return render(request, 'home.html')

def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('new')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        return redirect('loginn')
    return render(request, 'register.html')

def new(request):
    return render(request, 'new.html')

def final(request):
    return render(request, 'final.html')

def redirect_idukki(request):
    return redirect("https://en.wikipedia.org/wiki/Idukki_district")
def redirect_kottayam(request):
    return redirect("https://en.wikipedia.org/wiki/Kottayam")
def redirect_malappuram(request):
    return redirect("https://en.wikipedia.org/wiki/Malappuram")
def redirect_palakkad(request):
    return redirect("https://en.wikipedia.org/wiki/Palakkad")
def redirect_kochi(request):
    return redirect("https://en.wikipedia.org/wiki/Kochi")