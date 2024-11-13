from django.shortcuts import render, redirect

from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm

# Create your views here.
def login(request):
    # request의 method에 따라서 처리해야 할 코드가 다르다.
    # method == "GET" : 로그인 화면
    # mehotd == "POST" : 사용자가 입력한 ID/PW 검사해서 로그인 처리

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 유효성 검사 통과 : 로그인
            auth_login(request, form.get_user())
            return redirect("todos:index")
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)