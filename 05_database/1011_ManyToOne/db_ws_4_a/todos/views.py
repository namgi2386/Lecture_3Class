from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    print(request.user.is_authenticated)
    todo_list = Todo.objects.all()
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todos/index.html', context)

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False) # 데이터베이스 저장 x, 인스턴스만 생성
            todo.user = request.user # form 에서 입력할 수 없는 user 정보 직접 넣기
            todo.save() # 이제 저장 가능
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm()
    context = {
        'form': form
    }
    return render(request, 'todos/create.html', context)
    
def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todos:index')
    else:
        return redirect('todos:detail', todo.pk)

def update(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm(instance=todo)
    context = {
        'todo': todo,
        'form': form
    }
    return render(request, 'todos/update.html', context)