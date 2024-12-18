from django.contrib.auth import get_user_model
from django.db import models

from books.models import Book

User = get_user_model()


class PublishingPlan(models.Model):
    STATUS_CHOICES = [
        ("not_started", "Not Started"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]
    id: models.BigAutoField = models.BigAutoField(primary_key=True)
    planning_start_date: models.DateField = models.DateField()
    planning_end_date: models.DateField = models.DateField()
    status: models.CharField = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="not_started"
    )
    user: models.ForeignKey = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="publishing_plans"
    )

    def __str__(self):
        return f"Publishing Plan for {self.id}"
