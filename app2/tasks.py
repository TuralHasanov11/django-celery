from celery.utils.log import get_task_logger
from .email import send_review_email
from celery import shared_task

logger = get_task_logger(__name__)

@shared_task(name="send_review_email_task")
def send_review_email_task(name, email, review):
  logger.info("email sent")
  return send_review_email(name, email, review)
