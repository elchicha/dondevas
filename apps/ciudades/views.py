from django.views.generic import TemplateView


class PaginaInicioView(TemplateView):
    template_name = 'ciudades/inicio.html'