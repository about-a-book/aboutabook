from django.contrib import admin
from django.urls import include, path

from config.schema import schema_view

from .views import MainPageView

urlpatterns = [
    # default
    path("", MainPageView.as_view(), name="main"),
    # admin
    path("admin/", admin.site.urls),
    # Swagger
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # summernote
    path("summernote/", include("django_summernote.urls")),
    # include
    path("publishing_plan/", include("publishing_plan.urls")),  # 신간 기획 관리
    path("user/", include("user.urls")),  # 유저 관리
]
