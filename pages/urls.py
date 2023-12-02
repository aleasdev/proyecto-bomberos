from django.urls import path
from .views import HomePageView, InvPageView, AsisPageView, InicioPageView, RegistroPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("inventario/", InvPageView.as_view(), name="inventario"),
    path("asistencia/", AsisPageView.as_view(), name="asistencia"),
    path("iniciosesion/", InicioPageView.as_view(), name="iniciosesion"),
    path("registro/", RegistroPageView.as_view(), name="registro"),
    
]