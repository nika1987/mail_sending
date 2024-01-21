from django.utils import timezone
from django.db import models
from client.models import Client
from users.models import User

# Constants

NULLABLE = {'blank': True, 'null': True}


class PeriodMail(models.TextChoices):
    DAYLE = "DY", 'Раз в день'
    WEEKLY = "WK", 'Раз в неделю'
    MONTLY = "MY", 'Раз в месяц'


class StatusMail(models.TextChoices):
    CREATED = "CR", 'Создана'
    RUNNING = "RU", 'Запущена'
    COMPLETED = "CO", 'Завершена'


class StatusLog(models.TextChoices):
    SUCCESS = "SU", 'Успешно'
    FAILURE = "FA", 'Ошибка'



class MailDistribution(models.Model):

    period_in_time = models.CharField(max_length=10, choices=PeriodMail.choices,  verbose_name='Периодичность рассылки')
    status = models.CharField(max_length=10, choices=StatusMail.choices, verbose_name='Статус рассылки')
    status_log = models.CharField(max_length=10, choices=StatusLog.choices, verbose_name='Статус попытки')

    def str(self):
        return self.period_in_time

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('period_in_time',)
# Message


class Message(models.Model):
    """Сообщение для рассылки"""
    title = models.CharField(max_length=100, verbose_name='Тема письма')
    text = models.TextField(verbose_name='Тело письма')
    #owner = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец"')

    def str(self):
        return self.title

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'
        ordering = ('title',)




class Mailing(models.Model):
    '''Рассылка'''
    title = models.CharField(max_length=100, verbose_name='Название')
    client = models.ManyToManyField(Client, verbose_name='Клиенты для рассылки')
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Сообщение')
    time_mail = models.DateTimeField(default=timezone.now, verbose_name='Время рассылки')
    period_mail = models.CharField(max_length=50, verbose_name='Период рассылки', choices=PeriodMail.choices)
    status_mail = models.CharField(max_length=50, default='created', verbose_name='Статус рассылки',
                                   choices= StatusMail.choices)
    #owner = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    def str(self):
        return self.title

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('time_mail',)


class Log(models.Model):
    '''Логи рассылки'''
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, **NULLABLE, verbose_name='Рассылка')
    datetime_attempt = models.DateTimeField(default=timezone.now, verbose_name='Дата последней попытки')
    status_attempt = models.CharField(choices=StatusLog.choices, max_length=50, verbose_name='Статус попытки')
    answer_server = models.TextField(**NULLABLE, verbose_name='Ответ сервера')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, **NULLABLE, verbose_name='Сообщение')

    def str(self):
        return f"Время рассылки: {self.datetime_attempt}"

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
        ordering = ('datetime_attempt',)