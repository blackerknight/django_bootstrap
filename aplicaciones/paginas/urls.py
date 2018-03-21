from django.conf.urls import url
from aplicaciones.paginas import views

urlpatterns = [
    url(r'^home/$', views.HomePageView.as_view(), name='home'),
    url(r'^password_change/$', views.HomePageView.as_view(), name='password_change'),
    url(r'^logout/$', views.HomePageView.as_view(), name='logout'),
    url(r'^login/$', views.HomePageView.as_view(), name='login'),

]
