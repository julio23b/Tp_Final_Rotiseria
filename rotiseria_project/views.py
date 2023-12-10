from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = "index.html"

class EspecialidadesPage(TemplateView):
    template_name = "especialidades.html"

class ContactoPage(TemplateView):
    template_name = "contacto.html"

