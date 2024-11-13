from django.shortcuts import render

# Create your views here.
def index(request):

    # 사용자에게 보여줄 결과 페이지(화면)
    return render(request, "todos/index.html")