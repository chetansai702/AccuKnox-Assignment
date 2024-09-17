from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
import logging
import time

logger = logging.getLogger(__name__)

@receiver(post_save, sender='yourapp.MyModel')  # Replace 'yourapp.MyModel' with your actual model
def my_handler(sender, instance, **kwargs):
    logger.info('Handler started at %s', time.strftime('%X'))
    # Modify the database to demonstrate transaction behavior
    with transaction.atomic():
        # Simulate a database change
        instance.name = 'Changed by signal'
        instance.save()
    logger.info('Handler finished at %s', time.strftime('%X'))
