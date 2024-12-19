from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, *args, **kwargs):
        if not email:
            raise ValueError("이메일을 입력하세요.")
        if not username:
            raise ValueError("사용자 이름을 입력하세요.")

        email = self.normalize_email(email)
        user = self.model(
            email=self.normalize_email(email), username=username, *args, **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, *args, **kwargs):
        user = self.create_user(email, password, *args, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username: models.CharField = models.CharField(
        max_length=20,
        unique=False,
        help_text="사용자 이름을 입력하세요.",
    )
    id: models.BigAutoField = models.BigAutoField(primary_key=True)
    login_id: models.CharField = models.CharField(
        unique=True, max_length=20, null=False, blank=False
    )
    email = models.EmailField(unique=True)  # 이메일 필드를 유일값으로 설정
    is_active = models.BooleanField(default=True)  # 활성 상태
    is_staff = models.BooleanField(default=False)  # 관리자 여부
    date_joined = models.DateTimeField(auto_now_add=True)  # 계정 생성 날짜

    objects = UserManager()  # type: ignore
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
