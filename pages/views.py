from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name ="home.html"

class InvPageView(TemplateView):
    template_name ="inventario.html"

class AsisPageView(TemplateView):
    template_name ="asistencia.html"

class InicioPageView(TemplateView):
    template_name ="inicio.html"

class RegistroPageView(TemplateView):
    template_name ="registro.html"