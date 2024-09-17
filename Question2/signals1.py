from django.db.models.signals import post_save
from django.dispatch import receiver
import threading
import time
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender='yourapp.MyModel')  # Replace 'yourapp.MyModel' with your actual model
def my_handler(sender, instance, **kwargs):
    logger.info('Handler started at %s on thread %s', time.strftime('%X'), threading.get_ident())
    time.sleep(5)  # Simulate a long-running task
    logger.info('Handler finished at %s on thread %s', time.strftime('%X'), threading.get_ident())
