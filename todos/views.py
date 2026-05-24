from django.shortcuts import render, redirect
from .models import Todo
from django.http import JsonResponse
from .forms import TodoForm


# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    print(todos)

    return render(request, "todos/list.html", {"todos": todos})


def todo_delete(request, id):
    try:
        todo = Todo.objects.get(id=id)
        print(todo)
        todo.delete()

    except:
        print("無此ID")
    return redirect("todo_list")


def todo_create(request):
    return render(request, "todos/create.html", {"form": TodoForm()})


def todo_return(request):
    return render(request, "todo-field", {"form": TodoForm()})
