import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import PublishingPlan

User = get_user_model()


class PublishingPlanAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        self.plan = PublishingPlan.objects.create(
            title="Test Plan",
            description="This is a test plan.",
            start_date="2024-01-01",
            end_date="2024-12-31",
            status="not_started",
            user=self.user
        )

    def test_list_publishing_plans(self):
        response = self.client.get('/publishing_plan/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_publishing_plan(self):
        data = {
            "title": "New Plan",
            "description": "A new plan for testing.",
            "start_date": "2024-01-01",
            "end_date": "2024-12-31",
            "status": "in_progress"
        }
        response = self.client.post('/publishing_plan/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_publishing_plan(self):
        data = {"status": "completed"}
        response = self.client.patch(f'/publishing_plan/{self.plan.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_publishing_plan(self):
        response = self.client.delete(f'/publishing_plan/{self.plan.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
