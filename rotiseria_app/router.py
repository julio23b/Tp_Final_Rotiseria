from rest_framework import routers
from .viewsets import PedidoViewSets

router = routers.SimpleRouter()
router.register("api_rotiseria",PedidoViewSets)