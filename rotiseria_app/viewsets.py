from rest_framework.viewsets import ModelViewSet
from .models import Pedido
from .serializers import PedidoSerializer

class PedidoViewSets(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer