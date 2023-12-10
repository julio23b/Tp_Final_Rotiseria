from rest_framework.serializers import ModelSerializer
from .models import Pedido

class PedidoSerializer(ModelSerializer):
    class Meta: 
        model = Pedido
        fields = "__all__"
        