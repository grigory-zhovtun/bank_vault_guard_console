import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    passcard_all = Passcard.objects.all()

    object_fields = {
        'is_active': passcard_all[0].is_active,
        'created_at': passcard_all[0].created_at,
        'passcode': passcard_all[0].passcode,
        'owner_name': passcard_all[0].owner_name,
    }

    active_passcard = Passcard.objects.filter(is_active=True)

    print(f'Всего пропусков {Passcard.objects.count()}')
    print(f'Активных пропусков {len(active_passcard)}') # noqa: T001
