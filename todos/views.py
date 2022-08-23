from datetime import datetime
from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect
from django.contrib import messages
from .models import Todo as Task

def Home(request):
    if request.user.is_authenticated:
        return redirect('Todo')
    return render(request, 'Home.html')

def Login(request):
    if request.method=="POST":
        if (request.POST['Username']=="" and request.POST['Password']==""):
            messages.error(request, 'Username & Password cannot be empty')
            return redirect('/')
        else:
            user = authenticate(username=request.POST['Username'], password=request.POST['Password'])
            if user is not None:
                auth.login(request, user)
                return redirect('Todo')
            messages.error(request, 'Invalid Credentials')
            return redirect('/')
    return redirect('/')

def Logout(request):
    auth.logout(request)
    return redirect('/')

def Signup(request):
    if request.method == 'POST':
        if request.POST['Password'] == request.POST['ConfirmPassword']:
            try:
                User.objects.create_user(username=request.POST['Username'], email=request.POST['Email'], password=request.POST['Password'])
                user = authenticate(username=request.POST['Username'], password=request.POST['Password'])
                auth.login(request, user)
                return redirect('Todo')
            except IntegrityError as e: 
                messages.error(request, "Username already taken")
                return redirect('Signup')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('Signup')
    return render(request, 'Signup.html')

def Todo(request):
    if request.user.is_authenticated:
        return render(request, 'Todo.html', 
        {
        'Total':Task.objects.filter(user=request.user).count(),
        'Todos_here':Task.objects.filter(user=request.user).order_by("completed", "-created_at"),
        'Completed':Task.objects.filter(user=request.user, completed=True),
        'Remaining':Task.objects.filter(user=request.user).count()-Task.objects.filter(user=request.user, completed=True).count()
        })
    return render(request, 'Home.html')

def Createtodo(request):
    Todo = Task(user=request.user, todo=request.POST['Addtask'], created_at=datetime.now())
    Todo.save()
    messages.error(request, 'Task created')
    return redirect('Todo')

def Updatetodo(request, Todo_id):
    updatedtask=Task.objects.filter(id=Todo_id).update(todo=request.POST['updatetask'])
    messages.error(request, 'Task updated')
    return redirect('Todo')

def Deletetodo(request, Todo_id):
    Task.objects.get(id=Todo_id).delete()
    messages.error(request, 'Task deleted')
    return redirect('Todo')

def Completed(request, Todo_id):
    t = Task.objects.get(id=Todo_id)
    t.completed=True
    t.save()
    return redirect('Todo')

def Edit(request, Todo_id):
    return render(request, 'Edit.html', {'populate':Task.objects.get(id=Todo_id)})

def Uncompleted(request):
    return render(request, 'Todo.html', {
        'Total':Task.objects.filter(user=request.user).count(),
        'Todos_here':Task.objects.filter(user=request.user, completed=False).order_by("completed", "-created_at"),
        'Completed':Task.objects.filter(user=request.user, completed=False),
        'Remaining':Task.objects.filter(user=request.user).count()-Task.objects.filter(user=request.user, completed=True).count()
        })

def Redotodo(request, Todo_id):
    t = Task.objects.get(id=Todo_id)
    t.completed=False
    t.save()
    return redirect('Todo')

def Clear(request):
    Task.objects.filter(user=request.user).delete()
    return render(request, 'Todo.html', 
    {
        'Total':Task.objects.filter(user=request.user).count(),
        'Todos_here':Task.objects.filter(user=request.user).order_by("completed"),
        'Completed':Task.objects.filter(completed=True),
        'Remaining':(Task.objects.filter(user=request.user).count())-(Task.objects.filter(completed=True).count())
    })

def Search(request):
    if(request.method=="POST"):
        search_query=request.POST['Search']
        if(len(search_query)==0):
            return redirect('Todo')
        elif Task.objects.filter(user=request.user, todo__icontains=search_query) :
            messages.error(request, " Results for "+'"'+search_query+'" ')
            return render(request, 'Todo.html', {
                'value':search_query,
                'clear':'Clear Search',
                'Total':Task.objects.filter(user=request.user).count(),
                'Todos_here':Task.objects.filter(user=request.user, todo__icontains=search_query).order_by("completed", "-created_at"),
                'Completed':Task.objects.filter(user=request.user,completed=True),
                'Remaining':(Task.objects.filter(user=request.user).count())-(Task.objects.filter(user=request.user, completed=True).count())
                })
        else:
            messages.error(request, " No results for "+'"'+search_query+'" ')
            return redirect('Todo')
    return redirect('Todo')