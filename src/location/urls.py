from django.urls import path
from . import views


urlpatterns = [
path('camions/', views.camion_list, name='camion_list'),
        path('clients/', views.client_list, name='client_list'),
        path('louer_camion/<int:camion_id>/', views.louer_camion, name='louer_camion'),
]

