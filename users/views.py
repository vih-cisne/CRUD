from django.shortcuts import render, redirect
from .models import User

def home(request):
    users = User.objects.all()
    return render(request, "index.html", {"users": users})

def save(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    age = request.POST.get("age")

    User.objects.create(name = name, email = email, age = age)
    
    users = User.objects.all()
    return render(request, "index.html", {"users": users})

def edit(request, id):
    user = User.objects.get(id = id)

    return render(request, "update.html", {"user": user})

def update(request, id):
    name = request.POST.get("name")
    email = request.POST.get("email")
    age = request.POST.get("age")

    user = User.objects.get(id = id)

    user.name = name
    user.email = email
    user.age = age

    user.save()

    return redirect(home)

def delete(request,id):

    user = User.objects.get(id = id)
    user.delete()

    users = User.objects.all()
    return render(request, "index.html", {"users": users})



