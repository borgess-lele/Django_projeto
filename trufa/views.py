from rest_framework.viewsets import ModelViewSet

from trufa.models import Trufa
from trufa.serializers import TrufaSerializer

class TrufaViewSet(ModelViewSet):
    queryset = Trufa.objects.all()
    serializer_class = TrufaSerializer