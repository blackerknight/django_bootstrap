from django.conf.urls import url
from aplicaciones.paginas import views

urlpatterns = [
    url(r'^pagina1/$', views.HomePageView.as_view(), name='pagina1')
]
