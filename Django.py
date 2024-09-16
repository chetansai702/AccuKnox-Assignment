from django.db.models.signals import post_save
from django.dispatch import receiver

def my_receiver(sender, instance, **kwargs):
    print("Receiver function is running")
    # Simulate a long-running task
    import time
    time.sleep(5)

post_save.connect(my_receiver, sender=MyModel)

# Trigger the signal
my_instance = MyModel.objects.create(...)