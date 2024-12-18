from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Contractor(models.Model):
    ROLE_CHOICES = [
        ('author', 'Author'),
        ('translator', 'Translator'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="contractors")

    def __str__(self):
        return f"{self.name} ({self.role})"
