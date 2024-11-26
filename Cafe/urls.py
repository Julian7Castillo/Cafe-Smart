from django.urls import path
from .views import *





urlpatterns = [
    path('', index,name='index' ),
    path('servicios/', servicios,name='servicios' ),
    path('nosotros/', nosotros,name='nosotros' ),
    path('contactanos/', contactanos,name='contactanos' ),
    path('login/', Login,name='login' ),
    path('inicio/', inicio,name='inicio' ),
]


