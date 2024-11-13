from django.urls import path
from . import views

app_name = "diaries"

urlpatterns = [
    # 메인 화면 요청
    path("", views.index, name="index" ),
    # 일기장 생성 요청
    # GET => 일기장 생성 페이지를 응답
    # POST => 일기장 생성해서 DB에 저장 하고 INDEX로 
    path("create/", views.create, name="create"),
]
