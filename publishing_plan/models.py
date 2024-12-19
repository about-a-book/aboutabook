from django.contrib.auth import get_user_model
from django.db import models

import publishing_plan
from config.models import BaseModel
from contractor.models import Contractor

User = get_user_model()


class PublishingPlan(models.Model):
    STATUS_CHOICES = [
        ("진행 시작 전", "진행 시작 전"),
        ("진행 중", "진행 중"),
        ("완료", "완료"),
        ("홀딩", "홀딩"),
    ]
    id: models.BigAutoField = models.BigAutoField(primary_key=True)
    title: models.CharField = models.CharField(max_length=255)  # 기획 제목
    description: models.TextField = models.TextField(
        blank=True, null=True, default=""
    )  # 기획 설명
    start_date: models.DateField = models.DateField()
    end_date: models.DateField = models.DateField()
    status: models.CharField = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="not_started"
    )
    user: models.ForeignKey = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="publishing_plans"
    )
    contractors: models.ManyToManyField = models.ManyToManyField(  # 저자/번역가
        Contractor, related_name="publishing_plans", blank=True
    )

    def __str__(self):
        return f"{self.title} - {self.status}"


class Comment(BaseModel, models.Model):
    publishing_plan: models.ForeignKey = models.ForeignKey(
        PublishingPlan, on_delete=models.CASCADE, related_name="comments"
    )
    user: models.ForeignKey = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    message: models.TextField = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.user}: {self.message}"
