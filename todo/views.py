from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.contrib import messages
# import todo form and models
from .forms import TodoForm
from .models import Todo
# Create your views here.


def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                todo = form.save(commit=False)
                todo.author = request.user
                todo.save()
                messages.success(request, " Task added successfully!")
                return redirect('home')
            else:
                messages.error(request, "You must be logged in to add a task.")
        else:
            messages.error(request, "Error updating task!")
    form = TodoForm()
 
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)

   
@login_required
def removeTask(request, item_id):
    
    item = get_object_or_404(Todo, id=item_id)
    
    if request.user == item.author:
        if request.method == "POST":
            Todo.objects.filter(id=item_id).delete()
            return redirect('home')
        context = {}
        return render(request, 'todo/remove.html', context)
        
    
    else:
        messages.error(request, "You do not have permission to delete this Task.")
    
    return redirect('home')


@login_required
def edit_task(request, item_id):
    item = get_object_or_404(Todo, id=item_id)
    
    if request.user != item.author:
        messages.error(request, "You do not have permission to edit this task.")
        return redirect('home')

    if request.method == "POST":
        form = TodoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect('home')
    else:
        form = TodoForm(instance=item)

    context = {'form': form}
    return render(request, 'todo/edit.html', context)
