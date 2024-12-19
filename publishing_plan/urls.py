from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    CommentCreateView,
    CommentDeleteView,
    CommentUpdateView,
    PublishingPlanCreateView,
    PublishingPlanDeleteView,
    PublishingPlanDetailView,
    PublishingPlanListView,
    PublishingPlanUpdateView,
)

urlpatterns = [
    path("", PublishingPlanListView.as_view(), name="publishing-plan-list"),
    path(
        "<int:pk>/", PublishingPlanDetailView.as_view(), name="publishing-plan-detail"
    ),
    path(
        "create/",
        PublishingPlanCreateView.as_view(),
        name="publishing-plan-list-create",
    ),
    path(
        "<int:pk>/update/",
        PublishingPlanUpdateView.as_view(),
        name="publishing-plan-update",
    ),
    path(
        "<int:pk>/delete/",
        PublishingPlanDeleteView.as_view(),
        name="publishing-plan-delete",
    ),
    path(
        "comment/<int:publishing_plan_id>/create/",
        CommentCreateView.as_view(),
        name="comment-create",
    ),
    path(
        "comment/<int:publishing_plan_id>/update/",
        CommentUpdateView.as_view(),
        name="comment-update",
    ),
    path(
        "comment/<int:publishing_plan_id>/delete/",
        CommentDeleteView.as_view(),
        name="comment-delete",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
