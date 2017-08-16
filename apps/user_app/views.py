from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from models import *

def index(request):
    context = {
        "user_info": User.objects.all().values()
    }
    return render(request,'user_app/index.html', context)

def show(request, id):
    if request.method == "GET":
        context = {
            "user" : User.objects.get(id=id)
        }
        return render(request,'user_app/show.html', context)
    else:
        # TODO: find a way to pass id into the url when we redirecting

        return HttpResponse("hello!!")
        # request.session["id"]= User.objects.get(id=id).id
        #
        # return redirect("/user/update")

def update(request, id):
    user = User.objects.get(id=id)
    user.first_name = request.POST["f_name"]
    user.last_name = request.POST["l_name"]
    user.email = request.POST["email"]
    user.save()
    return redirect("/user")

def new(request):
    return render(request,'user_app/new.html')

def edit(request, id):
    context = {
        "user" : User.objects.get(id=id)
    }
    return render(request,'user_app/edit.html', context)

def create(request):
    data = User.objects.create(first_name=request.POST["f_name"], last_name=request.POST["l_name"], email=request.POST["email"])
    print data.first_name, data.last_name
    return redirect("/user/new")

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()

    return redirect("/user")
