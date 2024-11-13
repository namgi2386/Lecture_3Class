from django.shortcuts import render, redirect
from .models import Diary, Comment
from .forms import DiaryForm, CommentForm

# Create your views here.
def index(request):
    diaries = Diary.objects.all()
    comment_form = CommentForm()
    context = {
        'diaries': diaries,
        'comment_form': comment_form
    }
    return render(request, 'diaries/index.html', context)

def create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('diaries:index')
    else:
        form = DiaryForm()
    context = {
        'form': form
    }
    return render(request, 'diaries/create.html', context)

def comments_create(request, diary_pk):
    diary = Diary.objects.get(pk=diary_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.diary = diary
            comment.save()
    return redirect('diaries:index')

def comments_delete(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('diaries:index')

def likes(request, diary_pk):
    if request.method == "POST":
        diary = Diary.objects.get(pk=diary_pk)
        # 지금 요청을 보낸 사람이 이미 이 다이어리에 좋아요 표시를 했다면 => 좋아요 취소
        if request.user in diary.like_users.all():
            diary.like_users.remove(request.user)
        # 이 다이어리에 좋아요 표시를 안했으면 => 좋아요 추가
        else:
            diary.like_users.add(request.user)
    
    return redirect("diaries:index")