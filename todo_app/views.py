from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .models import *
from .forms import *
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User, auth
#Anonymous required
def anonymous_required(function=None, redirect_url=None):

   if not redirect_url:
       redirect_url = 'index'

   actual_decorator = user_passes_test(
       lambda u: u.is_anonymous,
       login_url=redirect_url
   )

   if function:
       return actual_decorator(function)
   return actual_decorator


@anonymous_required
def login(request):
    context = {}
    if request.method == 'GET':
        form = UserLoginForm()
        context['form'] = form
        return render(request, 'todo_app/login.html', context)

    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        all_user=User.objects.values('email')
        print(all_user)
        user = auth.authenticate(email=email, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)

            return redirect('index')
        else:
            context['form'] = form
            messages.error(request, 'Invalid Credentials')
            return redirect('login')


    return render(request, 'todo_app/login.html', context)


def index(request):
    all_todo=ToDoList.objects.all()
    all_items=all_todo
    count=all_items.count()
    all_todo_dates=ToDoList.objects.values('date').distinct()

    print(all_todo_dates)
    context={
        'all_todo_dates':all_todo_dates,
        'all_items':all_items,
        'count':count,
    }
    return render(request,'todo_app/index.html',context)



def logout_user(request):
    auth.logout(request)
    messages.error(request, 'Invalid Credentials')
    return redirect('login_user')




def login_user(request):

    return render(request,"todo_app/login.html")



def dologin(request):
    if request.method!="POST":
        print("not right")
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=RegisterUser.objects.filter(email=email,password=password)
        print(user)
        if user!=None and len(user)>0:
            #login(request, user)
            messages.success(request, "Valid Login Details")
            return redirect('index')

        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect('/')


def register_user(request):
    return render(request,'todo_app/register_user.html')


def register_user_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")

        try:
            chk_email=RegisterUser.objects.filter(email=email)
            print(chk_email)
            if len(chk_email)!=0:
                messages.error(request, "User with this email-id already exists!")
                return HttpResponseRedirect("/register_user")
            user_reg = RegisterUser(first_name=first_name, last_name=last_name, email=email,password=password,phone=phone)
            user_reg.save()
            messages.success(request, "Successfully Added New User!")
            return HttpResponseRedirect("/")
        except:
            messages.error(request, "Failed to Add New User!")
            return HttpResponseRedirect("/register_user")


def add_new_todo(request):
    user=request.user
    print(user)
    return render(request, 'todo_app/add_new_todo.html')

def save_new_todo(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        title = request.POST.get("title")
        date = request.POST.get("date")

        try:
            user_reg = ToDoList(date=date, todo=title)
            user_reg.save()
            messages.success(request, "Successfully Added to List!")
            return HttpResponseRedirect("/add_new_todo")
        except:
            messages.error(request, "Failed to Add!")
            return HttpResponseRedirect("/add_new_todo")


def edit_todo_item(request,todo_id):
    todo_item = ToDoList.objects.get(id=todo_id)
    curr_date=datetime.date.today()
    str_d=str(curr_date)
    print(type(str_d))
    print(type(todo_item.date))
    date=todo_item.date

    if str_d == date:
        return render(request, "todo_app/edit_todo_item.html", {"todo_item": todo_item})
    else:
        messages.info(request,"Not allowed to edit!")
        return HttpResponseRedirect("/index")


def edit_todo_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        todo_id = request.POST.get("title")
        done=request.POST.get("done")
        print(done)
        try:
            user_reg = ToDoList.objects.get(id=todo_id)
            if done=='Not Yet':
                user_reg.done=False
            if done=='Done':
                user_reg.done=True

            print(user_reg.done)
            user_reg.save()
            messages.success(request, "Successfully Edited!")
            return HttpResponseRedirect("/index")
        except:
            messages.error(request, "Failed to Edit Item!")
            return HttpResponseRedirect("/edit_todo_item/" + todo_id)


def remove_todo(request,todo_id):
    obj=ToDoList.objects.get(id=todo_id)
    obj.delete()
    return redirect("index")

def filter_todo(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        date = request.POST.get("date")
        todo = ToDoList.objects.filter(date=date).all()
        all_todo_dates=ToDoList.objects.values('date').distinct()
        print(todo)
        context={
                'all_todo_dates':all_todo_dates,
                'all_items':todo,
        }

        return render(request,'todo_app/index.html',context)

