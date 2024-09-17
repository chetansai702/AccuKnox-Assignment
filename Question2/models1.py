from django.db import models
import logging
import threading
import time

logger = logging.getLogger(__name__)

class MyModel(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        logger.info('Model save started at %s on thread %s', time.strftime('%X'), threading.get_ident())
        super().save(*args, **kwargs)
        logger.info('Model save finished at %s on thread %s', time.strftime('%X'), threading.get_ident())
