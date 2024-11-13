from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm


# Create your views here.
def index(request):
    todo_list = Todo.objects.all()
    # todo = Todo.objects.get(pk=10)
    context = {"todo_list": todo_list}
    return render(request, "todos/index.html", context)


def create(request):
    if request.method == "POST":
        # POST method로 들어온 요청 : DB에 todo 새로 만들어서 삽입요청
        # request.POST 안에 사용자가 입력한 데이터가 있다
        # 그 데이터를 통해 FORM 만들고 유효성 검사 후 통과하면 SAVE
        form = TodoForm(data=request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect("todos:detail", todo.pk)
        # 만약 유효성검사에 실패하면
        # form 객체(인스턴스)안에는 장고가 기록한 에러메세지가 들어있다.
        print(form)
    else:
        # POST 요청이 아니였다면 새로운 Todo 작성을 위해서
        # 빈 폼을 만들어 주면 된다.
        form = TodoForm()
    
    # 여기까지 왔다는 것은 POST 요청으로 들어왔으나 유효성 검사 통과하지못한경우
    # 아니면 POST 이외의 방식으로 요청이 들어왔을때
    # Todo 생성 화면을 보여주면 된다.
    context = {
        "form" : form
    }
    return render(request, "todos/create.html", context)


def detail(request, todo_pk):
    # todo = Todo.objects.get(pk=todo_pk)
    # 해당 todo가 없을때 try-catch로 상황대비
    todo = get_object_or_404(Todo, pk=todo_pk)
    context = {"todo": todo}
    return render(request, "todos/detail.html", context)


# def new_todo(request):
#     # work = request.POST.get("work")
#     # content = request.POST.get("content")
#     # is_completed = False
#     form = TodoForm(data=request.POST)
#     if form.is_valid():
#         todo = form.save()  # 이때 pk가 생성
#         return redirect("todos:detail", todo.pk)

#     # todo = Todo(work=work, content=content, is_completed=is_completed)
#     # todo.save()
#     # return redirect("todos:detail", todo.pk)
#     context = {"form": form}
#     return render(request, "todos/create_todo.html", context)


def delete_todo(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect("todos:index")


def update(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == "POST":
        form = TodoForm(data=request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            return redirect("todos:detail", todo.pk)
        print(form)
    else:
        form = TodoForm(instance=todo)

    # form = TodoForm(instance=todo)
    context = {
        "todo": todo,
        "form": form,
    }
    return render(request, "todos/update.html", context)


# def edit_todo(request, todo_pk):
#     todo = Todo.objects.get(pk=todo_pk)

#     # work = request.POST.get("work")
#     # content = request.POST.get("content")

#     # todo.work = work
#     # todo.content = content
#     # todo.save()

#     # data : 사용자가 입력한 data
#     # instance : db에 원래 있던 데이터(인스턴스)
#     form = TodoForm(data=request.POST, instance=todo)
#     if form.is_valid():
#         todo = form.save()
#         return redirect("todos:detail", todo.pk)

#     # 유효성 검사 실패
#     context = {
#         "todo" : todo,
#         "form" : form,
#     }
#     return render(request, "todos/update_todo.html", context)
