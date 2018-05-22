from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from conduit.apps.core.utils import generate_random_string

from .models import Article

@receiver(pre_save, sender=Article)
def create_slug_for_article(sender, instance, *args, **kwargs):

    MAX_SLUG_LEN = 255

    if instance and not instance.slug:
        slug = slugify(instance.title)
        
        # We don't want to have 2 articles with the same slug
        unique = generate_random_string()

        if len(slug) > MAX_SLUG_LEN:
            slug = slug[:MAX_SLUG_LEN]
        
        u_len = len(unique)

        while len(slug) + u_len + 1 > MAX_SLUG_LEN:
            parts = slug.split('-')

            if len(parts) is 1:
                # The slug has no hypens. To append the unique string we must
                # arbitrarly remove `len(unique)` characters from the end of
                # `slug`. Subtract one to account for extra hyphen.
                slug = slug[:MAX_SLUG_LEN - u_len - 1]
            else:
                slug = '-'.join(parts[:-1])
        
        instance.slug = slug + '-' + unique