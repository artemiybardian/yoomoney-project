from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Устанавливаем переменные окружения для Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

# Создаём приложение Celery
app = Celery('your_project')

# Загружаем настройки из Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически искать задачи в приложениях Django
app.autodiscover_tasks()
