from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PublishingPlanListView, PublishingPlanListCreateView, PublishingPlanDetailView

urlpatterns = [
    path('all/', PublishingPlanListView.as_view(), name='publishing-plan-list'),
    path('', PublishingPlanListCreateView.as_view(), name='publishing-plan-list-create'),
    path('<int:pk>/', PublishingPlanDetailView.as_view(), name='publishing-plan-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
