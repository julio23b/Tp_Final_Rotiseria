from django.urls import path
from . import views
from .router import router


urlpatterns = [
    
    path('', views.index_crud, name='index_crud'),
    path('Crear', views.PedidoCreateView.as_view(), name='Realizar_Pedido'),
    path('Modificar/<pk>', views.PedidoUpdateView.as_view(), name='Modificar_Pedido'),
    path('Borrar/<pk>', views.PedidoDeleteView.as_view(), name='Borrar_Pedido'),
    path('Ver', views.PedidoListview.as_view(), name='Visualizar_Pedido'),
    path('Detalle/<pk>', views.PedidoDetailView.as_view(), name='Detalle_Pedido'),

]

urlpatterns += router.urls