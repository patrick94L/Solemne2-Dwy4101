
from django.urls import path, include
from rest_framework import routers, serializers, viewsets, filters
from .models import Plan
from django_filters.rest_framework import DjangoFilterBackend

# Serializers define the API representation.
class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = ['title', 'price', 'minutes', 'internet']

# ViewSets define the view behavior.
class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'title']
    search_fields = ['id', 'title']

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'', PlanViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('planes/', include('planes.urls')),
]