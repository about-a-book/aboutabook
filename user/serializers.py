from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "login_id",
            "username",
            "password",
            "is_staff",
            "is_superuser",
        ]

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"],
            login_id=validated_data["login_id"],
        )
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
        ]
        read_only_fields = [
            "id",
            "username",
        ]

    def update(self, instance, validated_data):
        # 비밀번호가 있는 경우에만 비밀번호를 해시하여 업데이트
        if "password" in validated_data:
            instance.set_password(validated_data["password"])

        instance.email = validated_data.get("email", instance.email)
        instance.profile_image = validated_data.get(
            "profile_image", instance.profile_image
        )

        instance.save()


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        # 이메일 비밀번호로 사용자인증
        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("이메일 또는 비밀번호가 잘못되었습니다.")

        attrs["user"] = user
        return attrs
