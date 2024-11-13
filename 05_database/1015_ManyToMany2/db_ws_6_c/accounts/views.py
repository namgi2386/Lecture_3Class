from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .forms import LoginForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('todos:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('todos:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('accounts:login')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('todos:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)

def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/change_password.html', context)



def profile(request, username):
    # 프로필 페이지를 보고싶은 사용자 검색
    profile_user = get_user_model().objects.get(username=username)
    # 위의 유저가 좋아요 한 다이어리 목록 검색
    like_diaries = profile_user.diary_set.all()

    context = {
        'profile_user' : profile_user,
        'like_diaries' : like_diaries
    }

    return render(request, 'accounts/profile.html', context)


def subscribe(request, user_pk):
    if request.method == "POST":
        # request.user : 구독 요청을 하는 user
        # user_pk : 구독할 대상 user의 pk 번호
        subscribe_user = get_user_model().objects.get(pk=user_pk)

        # request.user 가 이미 subscribe_user 를 구독한 상태 : 구독 취소
        if request.user in subscribe_user.subscriber.all():
            subscribe_user.subscriber.remove(request.user)
        # request.user 가 subscribe_user 를 구독하지 않은 상태 : 구독 추가
        else:
            subscribe_user.subscriber.add(request.user)
        
    return redirect("accounts:profile", subscribe_user.username)