from rest_framework import serializers

from .models import PublishingPlan


class PublishingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublishingPlan
        fields = [
            "id",
            "title",
            "description",
            "start_date",
            "end_date",
            "status",
            "user",
            "contractors",
        ]
        read_only_fields = ["id", "user"]  # `id`와 `user`는 수정 불가
