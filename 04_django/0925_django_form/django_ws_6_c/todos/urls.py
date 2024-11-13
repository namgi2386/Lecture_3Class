from django.urls import path
from . import views


app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    # new 는 create 와 합쳐짐 
    # path('new_todo/', views.new_todo, name='new_todo'),
    path('<int:todo_pk>/', views.detail, name='detail'),
    path('<int:todo_pk>/delete/', views.delete_todo, name='delete_todo'),
    path('<int:todo_pk>/update/', views.update, name='update'),
    # edit 은 update 와 합쳐짐
    # path('<int:todo_pk>/edit_todo/', views.edit_todo, name='edit_todo'),
]