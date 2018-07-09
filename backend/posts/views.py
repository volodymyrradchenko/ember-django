import rest_framework.parsers
import rest_framework.renderers
from rest_framework import exceptions

import rest_framework_json_api.parsers
import rest_framework_json_api.metadata
from rest_framework_json_api.utils import format_drf_errors
from rest_framework_json_api.views import ModelViewSet


from posts.models import Post
from posts.serializers import PostSerializer


HTTP_422_UNPROCESSABLE_ENTITY = 422

class JsonApiViewSet(ModelViewSet):
    """
    This is an example on how to configure DRF-jsonapi from
    within a class. It allows using DRF-jsonapi alongside
    vanilla DRF API views.
    """
    parser_classes = [
        rest_framework_json_api.parsers.JSONParser,
        rest_framework.parsers.FormParser,
        rest_framework.parsers.MultiPartParser,
    ]
    renderer_classes = [
        rest_framework_json_api.renderers.JSONRenderer,
        rest_framework.renderers.BrowsableAPIRenderer,
    ]
    metadata_class = rest_framework_json_api.metadata.JSONAPIMetadata

    def handle_exception(self, exc):
        if isinstance(exc, exceptions.ValidationError):
            # some require that validation errors return 422 status
            # for example ember-data (isInvalid method on adapter)
            exc.status_code = HTTP_422_UNPROCESSABLE_ENTITY
        # exception handler can't be set on class so you have to
        # override the error response in this method
        response = super(JsonApiViewSet, self).handle_exception(exc)
        context = self.get_exception_handler_context()
        return format_drf_errors(response, context, exc)


class PostViewSet(JsonApiViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer