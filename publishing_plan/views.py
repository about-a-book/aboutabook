from django.http import Http404
from django.views.generic import ListView
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from .models import PublishingPlan
from .serializers import PublishingPlanSerializer


class PublishingPlanListCreateView(ListCreateAPIView):
    """
    Handles listing all publishing plans and creating a new one.
    """

    serializer_class = PublishingPlanSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        Optionally filter plans by user if needed.
        """
        return PublishingPlan.objects.all()

    def perform_create(self, serializer):
        """
        Automatically associate the logged-in user with the created publishing plan.
        """
        serializer.save(user=self.request.user)


class PublishingPlanListView(ListView):
    """
    전체 목록 조회
    """

    serializer_class = PublishingPlanSerializer
    permission_classes = [AllowAny]
    template_name = "todo_list.html"

    def get_queryset(self):
        """
        전체 목록을 조회합니다
        """
        return PublishingPlan.objects.all()


class PublishingPlanDetailView(RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a specific publishing plan.
    """

    serializer_class = PublishingPlanSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        Ensure only accessible objects are returned.
        """
        return PublishingPlan.objects.all()

    def get_object(self):
        """
        Retrieves the specific publishing plan.
        """
        obj = get_object_or_404(PublishingPlan, pk=self.kwargs.get("pk"))
        return obj
