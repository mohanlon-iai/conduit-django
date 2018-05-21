from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Article

@receiver(post_save, sender=Article)
def create_slug_for_article(sender, instance, created, *args, **kwargs):
    # Notice that we're checking for `created` here. We only want to do this
    # the first time the `Article` instance is created. If the save that caused
    # this signal to be run was an update action, we know the article already
    # has a slug.
    if instance and created:
        if not instance.slug:
            instance.slug = 'temp_slug'