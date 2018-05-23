from rest_framework import mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Article
from .renderers import ArticleJSONRenderer
from .serializers import ArticleSerializer


class ArticleViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):

    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ArticleSerializer
    renderer_classes = (ArticleJSONRenderer,)
    queryset = Article.objects.all()    #pylint: disable=no-member    