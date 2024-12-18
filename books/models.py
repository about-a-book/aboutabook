from django.contrib.auth import get_user_model
from django.db import models

from config.models import BaseModel
from contractor.models import Contractor

User = get_user_model()


class Book(BaseModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True)
    publication_date = models.DateField()
    price = models.FloatField()
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name="books")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="books")
    publishing_plan = models.OneToOneField("publishing_plan.PublishingPlan", on_delete=models.SET_NULL, null=True, blank=True, related_name="book")

    def __str__(self):
        return self.title
