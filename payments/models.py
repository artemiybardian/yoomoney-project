from django.db import models
from django.utils.timezone import now


class Phone(models.Model):
    provider = models.CharField(max_length=50)  # Провайдер
    modem_number = models.IntegerField()        # Номер модема
    phone_number = models.CharField(max_length=15)  # Номер телефона
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Абонентская плата
    payment_day = models.IntegerField()         # Число месяца для оплаты (1-31)

    def __str__(self):
        return f"{self.phone_number} - {self.provider}"


class Transaction(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),      # Ожидание оплаты
        ('success', 'Success'),      # Оплата успешна
        ('failed', 'Failed'),        # Ошибка оплаты
    ]

    phone = models.ForeignKey(
        Phone, on_delete=models.CASCADE, related_name='transactions')  # Связь с телефоном
    amount = models.DecimalField(
        max_digits=10, decimal_places=2)  # Сумма платежа
    # Дата и время создания транзакции
    created_at = models.DateTimeField(default=now)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')  # Статус транзакции
    yoomoney_transaction_id = models.CharField(
        max_length=100, blank=True, null=True)    # ID транзакции в YooMoney
    # Сообщение об ошибке (если есть)
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Transaction {self.id} for {self.phone.phone_number} - {self.status}"
