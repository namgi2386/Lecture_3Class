from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=12)
#     password = forms.CharField(widget=forms.PasswordInput())

# 간접 참조를 하는 이유 : User 클래스에 변경이 일어난 경우
# 현재 여기 코드는 수정할 필요가 없도록.
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User