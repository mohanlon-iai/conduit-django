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
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Article.objects.all()    #pylint: disable=no-member

    def create(self, request, *args, **kwargs):
        serializer_data = request.data.get('article', {})
        serializer_context = {'author': request.user.profile}

        serializer = self.serializer_class(
            data=serializer_data,
            context=serializer_context
        )

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
