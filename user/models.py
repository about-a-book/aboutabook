from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id: models.BigAutoField = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)  # 이메일 필드를 유일값으로 설정
    is_active = models.BooleanField(default=True)  # 활성 상태
    is_staff = models.BooleanField(default=False)  # 관리자 여부
    date_joined = models.DateTimeField(auto_now_add=True)  # 계정 생성 날짜

    def __str__(self):
        return self.username
