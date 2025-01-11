from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule


class Command(BaseCommand):
    help = 'Создание расписания для schedule_monthly_payments'

    def handle(self, *args, **kwargs):
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.DAYS,
        )

        task, created = PeriodicTask.objects.get_or_create(
            interval=schedule,
            name='Ежедневное выполнение schedule_monthly_payments',
            task='payments.tasks.schedule_monthly_payments',
        )

        if created:
            self.stdout.write(self.style.SUCCESS('Задача успешно создана!'))
        else:
            self.stdout.write(self.style.WARNING('Задача уже существует.'))
