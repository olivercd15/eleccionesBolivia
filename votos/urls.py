from django.urls import path
from . import views

urlpatterns = [
    path('', views.votos, name="Votos"),
    path('provincias.html/<int:dep_id>', views.provincias, name="Provincias"),
    path('municipios.html/<int:prov_id>', views.municipios, name="Municipios"),
    path('localidades.html/<int:mun_id>', views.localidades, name="Localidades"),
    path('recintos.html/<int:loc_id>', views.recintos, name="Recintos"),
    path('boleta.html/<int:rec_id>', views.boleta, name="Boleta"),
    path('datos_boleta.html/<int:bol_id>', views.datosBoleta, name="DatosBoleta"),
    path('export/<int:rec_id>',views.export, name="Export"),
    path('exportDatos/<int:bol_id>',views.exportDatos, name="ExportDatos"),
    path('api',views.api, name="Api")
]
