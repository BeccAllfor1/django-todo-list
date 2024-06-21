from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.contrib import messages
# import todo form and models
from .forms import TodoForm
from .models import Todo
# Create your views here.

@login_required
def index(request):
 
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            messages.success(request,"Todo item added successfully!")
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    form = TodoForm()
 
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)

   
@login_required
def remove(request, item_id):
    item = get_object_or_404(Todo, id=item_id)
    
    if request.user == item.author:
        item.delete()
        messages.info(request, "Item removed!")
    else:
        messages.error(request, "You do not have permission to delete this item.")
    
    return redirect('home')