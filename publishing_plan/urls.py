from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PublishingPlanViewSet

router = DefaultRouter()
router.register(r'', PublishingPlanViewSet, basename='publishing-plans')

urlpatterns = [
    path('', include(router.urls)),
]