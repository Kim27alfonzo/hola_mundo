from django.urls import path
from app1.views import hola_mundo
from app1.views import Adios_Mundo

urlpatterns = [
    path('', hola_mundo),
    path('app1/', Adios_Mundo.as_view()),
]