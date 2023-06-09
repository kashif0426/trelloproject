from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import *
from django.contrib.auth.decorators import*

@login_required 
def task(request):
    do_list = Task.objects.filter(do_status = True)
    working_list = Task.objects.filter(working_status = True)
    done_list = Task.objects.filter(done_status = True)
    do_count = do_list.count()
    working_count = working_list.count()
    done_count = done_list.count()
    
    context = {'do_list': do_list, 'working_list': working_list, 'done_list': done_list, 
               'do_count': do_count, 'working_count':working_count, 'done_count': done_count}
    return render(request, "task.html", context)

@login_required
def working(request):
    return redirect("/task")

@login_required
def move_working(request, id):
    obj = Task.objects.get(id = id)
    obj.working_status = True
    obj.do_status = False
    obj.save()
    return redirect ("/task")

@login_required
def move_to_done(request,id):
    obj = Task.objects.get(id = id)
    obj.done_status = True
    obj.working_status = False
    obj.save()
    return redirect ('/task')


def user_login(request):
    if request.method == "POST":
        
        username = request.POST["uname"]
        password = request.POST["psw"]
        print(password)
        user = authenticate(request, username = username, password = password)
        print(user)
        if user:
            user = login(request,user)
            return redirect("/task")
    return render(request, "login.html")

@login_required
def log_out(request):
    logout(request)
    return redirect("login")