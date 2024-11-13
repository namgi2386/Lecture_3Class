from django.shortcuts import render, redirect
from .models import Diary
from .forms import DiaryForm

import os
from django.conf import settings
from django.http.response import FileResponse


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
        form = DiaryForm(data=request.POST, files=request.FILES)
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


def download(request, diary_pk):
    diary = Diary.objects.get(pk=diary_pk)

    # 파일이 어디 있나? 경로 알아 내고
    file_path = os.path.join(settings.MEDIA_ROOT, diary.picture.path)

    # 경로를 통해서 파일을 연다.
    image = open(file_path, "rb")

    # 파일 전용 응답 객체로 응답
    # as_attatchment=True
    return FileResponse(image, as_attachment=True)