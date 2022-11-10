from django.conf import settings
from django.core.mail import send_mail

send_mail('', 'Доброе утро и хорошего дня (это автоматическая рассылка для автоматизации личных отношений)))', settings.EMAIL_HOST_USER, ['AVPavlenko@nvate.ru', 'collotun@gmail.com'])