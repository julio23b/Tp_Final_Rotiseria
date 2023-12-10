from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy

from .models import Pedido
# Create your views here.

def index_crud(request):
    context = {
        
    }
    return render(request, 'web/index_crud.html', context)

class PedidoListview(ListView):
    model = Pedido
    context_object_name = 'Pedido_Listado'
    template_name = 'web/Visualizar_Pedido.html'

class PedidoCreateView(CreateView):
    model = Pedido
    template_name = 'web/Realizar_Pedido.html'
    success_url = 'Ver'
    fields = '__all__'

class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'web/Detalle_Pedido.html'

class PedidoUpdateView(UpdateView):
    model = Pedido
    template_name = 'web/Modificar_Pedido.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('Pedido_Listado', kwargs={'pk': self.object.pk})

class PedidoDeleteView(DeleteView):
    model = Pedido
    template_name = 'web/Borrar_Pedido.html'
    success_url = reverse_lazy('Visualizar_Pedido')


