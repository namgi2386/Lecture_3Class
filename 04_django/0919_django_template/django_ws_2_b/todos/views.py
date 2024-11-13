from django.shortcuts import render

# Create your views here.
def index(request):
    # 사용자가 GET method로 보낸 요청 데이터 중에 name 이 "work" 인 데이터 찾아오기
    todo_title = request.GET.get("work")

    # 페이지에 담을 데이터 뭉치
    context = {
        "work" : todo_title
    }

    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')