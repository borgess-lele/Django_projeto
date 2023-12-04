from rest_framework.serializers import ModelSerializer,SlugRelatedField 
from uploader.models import Image
from uploader.serializers import ImageSerializer
from trufa.models import Trufa

class TrufaSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="imagem",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    imagem = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Trufa
        fields = "__all__"


class TrufaDetailSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)

    class Meta:
        model = Trufa
        fields = "__all__"

class TrufaListSerializer(ModelSerializer):
    imagem = ImageSerializer(required=False)
    class Meta:
        model = Trufa
        fields = ["id", "nome", "preco", "imagem",]