from django.shortcuts import render, redirect
from .models import Diary
from .forms import DiaryForm


# Create your views here.
def index(request):
    diaries = Diary.objects.all()
    context = {
        "diaries": diaries,
    }
    return render(request, "diaries/index.html", context)


def create(request):

    # 요청이 POST로 왔니?
    if request.method == "POST":
        # 일기장 FORM 생성
        form = DiaryForm(data=request.POST)
        # 유효성 검사 통과 하면 DB에 저장
        if form.is_valid():
            form.save()
            return redirect("diaries:index")
    # POST 가 아닌 다른 요청
    else:
        # 빈 폼 생성
        form = DiaryForm()
    
    context = {
        "form" : form
    }
    return render(request, "diaries/create.html", context)