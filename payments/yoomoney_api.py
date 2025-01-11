from yoomoney import Client
from yoomoney_project.config import YOOMONEY_ACCESS_TOKEN


ACCESS_TOKEN = YOOMONEY_ACCESS_TOKEN

client = Client(ACCESS_TOKEN)

def send_payment(phone_number, amount):
    try:
        # Формируем запрос на оплату
        request = client.account_info()
        payment = client.request_payment({
            "pattern_id": "phone-topup",  # Пополнение телефона
            "phone-number": phone_number,
            "amount": amount,
            "test_payment": True  # Для тестов (убрать в продакшене)
        })

        # Подтверждаем запрос
        confirmation = client.process_payment({
            "request_id": payment.request_id
        })

        if confirmation.status == "success":
            return {
                "status": "success",
                "transaction_id": confirmation.payment_id
            }
        else:
            return {
                "status": "failed",
                "error_message": confirmation.error
            }
    except Exception as e:
        return {
            "status": "failed",
            "error_message": str(e)
        }
