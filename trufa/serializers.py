from rest_framework.serializers import ModelSerializer

from trufa.models import Trufa

class TrufaSerializer(ModelSerializer):
    class Meta:
        model = Trufa
        fields = "__all__"