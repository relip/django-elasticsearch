from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import DefaultRouter

from django_elasticsearch.tests.models import TestModel
from django_elasticsearch.contrib.restframework import AutoCompletionMixin
from django_elasticsearch.contrib.restframework import IndexableModelMixin


class TestViewSet(AutoCompletionMixin, IndexableModelMixin, ModelViewSet):
    model = TestModel
    filter_fields = ('username',)
    ordering_fields = ('id',)
    search_param = 'q'
    paginate_by = 10
    paginate_by_param = 'page_size'

router = DefaultRouter()
router.register(r'tests', TestViewSet)
urlpatterns = router.urls
