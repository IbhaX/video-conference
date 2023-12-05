from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Recent

# Create your views here.


def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
        else:
            error_message = form.errors.as_text()
            return render(request, "register.html", {"error": error_message})

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is None:
            return render(
                request,
                "login.html",
                {"error": "Invalid credentials. Please try again."},
            )

        login(request, user)
        return redirect("/dashboard")
    return render(request, "login.html")


@login_required
def dashboard(request):
    recent = Recent.objects.all()
    return render(
        request, "dashboard.html", {"name": request.user.first_name, "recent": recent}
    )


@login_required
def videocall(request):
    recent = Recent(user=request.user)
    recent.save()
    return render(
        request,
        "videocall.html",
        {"name": f"{request.user.first_name} {request.user.last_name}"},
    )


@login_required
def logout_view(request):
    logout(request)
    return redirect("/login")


@login_required
def join_room(request):
    if request.method == "POST":
        roomID = request.POST["roomID"]
        return redirect(f"/meeting?roomID={roomID}")
    return render(request, "joinroom.html")
