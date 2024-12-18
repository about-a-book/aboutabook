from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import PublishingPlan
from .serializers import PublishingPlanSerializer


class PublishingPlanViewSet(viewsets.ViewSet):
    """
    A viewset for CRUD operations on PublishingPlan.
    """

    def list(self, request):
        queryset = PublishingPlan.objects.all()
        serializer = PublishingPlanSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        plan = get_object_or_404(PublishingPlan, pk=pk)
        serializer = PublishingPlanSerializer(plan)
        return Response(serializer.data)

    def create(self, request):
        serializer = PublishingPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):  # PATCH 요청 처리
        plan = get_object_or_404(PublishingPlan, pk=pk)
        serializer = PublishingPlanSerializer(plan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        plan = get_object_or_404(PublishingPlan, pk=pk)
        plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
