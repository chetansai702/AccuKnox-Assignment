from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
import time
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender='yourapp.ModelName')  # Replace 'yourapp.ModelName' with your actual model
def my_handler(sender, instance, **kwargs):
    logger.info('Handler started')
    time.sleep(5)  # Simulate a long-running task
    logger.info('Handler finished')
