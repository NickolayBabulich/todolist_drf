from rest_framework import serializers
from users.models import User
from users.validators import validate_string_field


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        max_length=15,
        validators=[validate_string_field],
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'password')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class UserUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        max_length=15,
        validators=[validate_string_field],
    )
    last_name = serializers.CharField(
        max_length=15,
        validators=[validate_string_field],
    )
    current_password = serializers.CharField(write_only=True, required=False)
    new_password = serializers.CharField(write_only=True, required=False)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        current_password = validated_data.get('current_password')
        new_password = validated_data.get('new_password')

        if current_password and new_password:
            if not instance.check_password(current_password):
                raise serializers.ValidationError('Current password is incorrect.')
            instance.set_password(new_password)

        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'current_password', 'new_password')
