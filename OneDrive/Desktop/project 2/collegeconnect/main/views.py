from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Event, Registration
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)
            role = user.profile.role

            if role == "student":
                return redirect("student_dashboard")
            elif role == "college":
                return redirect("college_dashboard")
            else:
                return redirect("admin_dashboard")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")
def student_dashboard(request):
    return render(request, 'student_dashboard.html')


def college_dashboard(request):
    return render(request, 'college_dashboard.html')


def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
        
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register')

        user=User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        from .models import Profile
        role=request.POST['role']
        Profile.objects.create(
            user=user,
            role=role
        )

        messages.success(request, "Registration successful! Please login.")
        return redirect('login')

    return render(request, 'register.html')
from .models import Event

from .forms import EventForm

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('events')
    else:
        form = EventForm()

    return render(request, 'create_event.html', {'form': form})
def events(request):
    events = Event.objects.all()
    return render(request, 'event.html', {'events': events})
def event_detail(request, id):
    event = Event.objects.get(id=id)
    return render(request, 'event_detail.html', {'event': event})
from django.shortcuts import get_object_or_404, redirect
from .models import Event, Registration

def register_event(request, id):
    event = get_object_or_404(Event, id=id)

    # avoid duplicate registration
    already_registered = Registration.objects.filter(
        student=request.user,
        event=event
    ).exists()

    if not already_registered:
        Registration.objects.create(
            student=request.user,
            event=event
        )

    return redirect('event_detail', id=event.id)
from .models import Registration

from django.contrib.auth.decorators import login_required

@login_required
def my_events(request):
    registrations = Registration.objects.filter(student=request.user)
    return render(request, "my_events.html", {"registrations": registrations})

def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def college_dashboard(request):
    return render(request, 'college_dashboard.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
def contact(request):
    return render(request, "contact.html")