from django.core.management.base import BaseCommand
from payments.models import Phone
from payments.services import process_payment


class Command(BaseCommand):
    help = 'Проверяет и запускает задачу для оплаты телефонов на сегодня'

    def handle(self, *args, **kwargs):
        phone = Phone.objects.get(phone_number=9376287268)
        process_payment.delay(phone.id)
        self.stdout.write(self.style.SUCCESS(
            'Задача для проверки оплаты телефонов была выполнена.'))
