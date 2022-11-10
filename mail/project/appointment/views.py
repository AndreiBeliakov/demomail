from django.conf import settings
from django.core.mail import send_mail

send_mail('', '', settings.EMAIL_HOST_USER, ['collotun@gmail.com'])