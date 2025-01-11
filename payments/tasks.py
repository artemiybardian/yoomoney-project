from celery import shared_task
from .models import Phone
from datetime import datetime
from .services import process_payment


@shared_task
def schedule_monthly_payments():
    """
    Проверяет телефоны с оплатой на сегодня и создаёт задачи для их оплаты.
    """
    today = datetime.today().day
    phones_to_pay = Phone.objects.filter(payment_day=today)
    count = phones_to_pay.count()

    if count == 1:
        phone = phones_to_pay.first()
        process_payment.delay(phone.id)
        print(f"Создана задача для телефона: {phone.phone_number}.")
    elif count > 1:
        for phone in phones_to_pay:
            process_payment.delay(phone.id)
        print(f"Создано {count} задач для оплаты телефонов.")
    else:
        print("Сегодня нет телефонов для оплаты.")
