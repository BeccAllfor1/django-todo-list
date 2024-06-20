from django.shortcuts import render, redirect
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
            form.save()
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

    ### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('home')

 