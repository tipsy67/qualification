
from appointment.src.mailers import sendmail_cmd
from celery import shared_task



@shared_task
def sendmail(recipients_emails: list, title: str, content: str):
    sendmail_cmd(recipients_emails, title, content)


