from pathlib import Path
from django.db.models.signals import pre_delete
from .models import BagModel
from django.dispatch import receiver

@receiver(pre_delete, sender=BagModel)
def pre_delete_bag(sender, instance, **kwargs):
    for img in instance.images.all():
        path = Path(img.image.path)
        print(path)
        if path.is_file():
            path.unlink()