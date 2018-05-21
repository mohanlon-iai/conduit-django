from django.db import models

from conduit.apps.core.models import TimestampedModel


class Article(TimestampedModel):
    title = models.CharField(db_index=True, max_length=255, unique=True)
    slug = models.CharField(db_index=True, max_length=255)

    body = models.TextField(blank=True)
    description = models.TextField(blank=True)

    author = models.ForeignKey(
        'profiles.Profile', 
        on_delete=models.CASCADE,
        related_name='articles'
    )

    def __str__(self):
        return self.title