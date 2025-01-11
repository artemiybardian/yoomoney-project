from celery import shared_task
from .models import Phone, Transaction
from yoomoney_api import send_payment


@shared_task
def process_payment(phone_id):
    """
    Процесс оплаты через YooMoney.
    """
    try:
        # Получаем телефон
        phone = Phone.objects.get(id=phone_id)

        # Создаём запись транзакции со статусом 'pending'
        transaction = Transaction.objects.create(
            phone=phone,
            amount=phone.amount,
            status='pending'
        )

        # Отправляем платеж через YooMoney API
        yoomoney_response = send_payment(phone.phone_number, phone.amount)

        # Обновляем статус транзакции в зависимости от ответа API
        if yoomoney_response['status'] == 'success':
            transaction.status = 'success'
            transaction.yoomoney_transaction_id = yoomoney_response['transaction_id']
        else:
            transaction.status = 'failed'
            transaction.error_message = yoomoney_response.get(
                'error_message', 'Unknown error')

        transaction.save()

    except Phone.DoesNotExist:
        print(f"Телефон с ID {phone_id} не найден.")
    except Exception as e:
        # Логируем ошибку и обновляем транзакцию как 'failed'
        transaction.status = 'failed'
        transaction.error_message = str(e)
        transaction.save()
        print(f"Ошибка при оплате телефона {phone_id}: {e}")
