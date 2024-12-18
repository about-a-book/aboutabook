from config.schema import schema_view
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # admin
    path("admin/", admin.site.urls),

    # Swagger
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

    # include
    path("publishing_plan/", include("publishing_plan.urls")),
]
