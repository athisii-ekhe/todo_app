from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = TodoForm()

    context = {
        'todo': Todo.objects.all(),
        'form': form
    }
    return render(request, 'todo/index.html', context)


def complete_todo(request, id):
    todo = Todo.objects.get(pk=id)
    todo.completed = True
    todo.save()
    return redirect('index')


def delete_completed_todo(request):
    Todo.objects.filter(completed__exact=True).delete()
    return redirect('index')


def delete_all(request):
    Todo.objects.all().delete()
    return redirect('index')


def nav(request):
    return render(request, 'todo/nav.html')
