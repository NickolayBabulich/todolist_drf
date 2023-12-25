from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@app.com',
            first_name='Elon',
            last_name='Mask',
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )

        user.set_password('1')
        user.save()
        print(f'Создан администратор:\n'
              f'Пользователь: {user.email}, пароль: 1\n')
