from django.core.mail import send_mail
from datetime import datetime, timedelta

from client.models import Client
from mail_sending.models import Message, Mailing, Log
from users.models import User

from config import settings


def send_mailing(mailing_object: Mailing):
    emails = [client.email for client in mailing_object.client.all()]
    try:
        send_mail(
            subject=mailing_object.message,
            message=mailing_object.message.message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=emails
        )
        status_attempt = 'success'
        answer_server = 'Email sent successfully'
    except Exception as e:
        status_attempt = 'error'
        answer_server = str(e)
    Log.objects.create(message=mailing_object.message,
                       status_attempt=status_attempt,
                       answer_server=answer_server)


def daily_send():
    '''Ежедневная рассылка'''
    for item in Mailing.objects.filter(period_mail='daily'):
        item.status_mail = 'running'
        item.save()
        send_mailing(item)
        item.status_mail = 'completed'
        item.save()


def weekly_send():
    '''Еженедельная рассылка'''
    for item in Mailing.objects.filter(period_mail='weekly'):
        item.status_mail = 'running'
        item.save()
        send_mailing(item)
        item.status = 'completed'
        item.save()


def monthly_send():
    '''Ежемесячная рассылка'''
    for item in Mailing.objects.filter(period_mail='monthly'):
        item.status_mail = 'running'
        item.save()
        send_mailing(item)
        item.status_mail = 'completed'
        item.save()
