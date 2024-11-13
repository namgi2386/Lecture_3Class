"""
URL configuration for todo_list_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from todos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # todo 앱과 관련된 기능은 todos/ 경로를 통해..
    # todos 앱의 urls.py 에 있는 url include
    path('todos/', include("todos.urls")),
    
    path("accounts/", include("accounts.urls")),
]
