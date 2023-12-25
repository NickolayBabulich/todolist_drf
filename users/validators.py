from rest_framework.serializers import ValidationError


def validate_string_field(value):
    if not value.isalpha():
        raise ValidationError('Поле должно содержать только буквы, пожалуйста введите корректное значение')
