import csv
import json

from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from votos.serializer import DepSerializer
from votos.models import Departamento, Provincia, Municipio, Localidad, Recinto, Boleta

# Create your views here.

def votos(request):
    departamentos = Departamento.objects.all()
    return render(request, "votos/votos.html",{"departamentos": departamentos})

def provincias(request, dep_id):
    provincias = Provincia.objects.filter(departamento_id=dep_id)
    return render(request, "votos/provincias.html",{"provincias": provincias})

def municipios(request, prov_id):
    municipios = Municipio.objects.filter(provincia_id=prov_id)
    return render(request, "votos/municipios.html",{"municipios": municipios})

def localidades(request, mun_id):
    localidades = Localidad.objects.filter(municipio_id=mun_id)
    return render(request, "votos/localidades.html",{"localidades": localidades})

def recintos(request, loc_id):
    recintos = Recinto.objects.filter(localidad_id=loc_id)
    return render(request, "votos/recintos.html",{"recintos": recintos})

def boleta(request, rec_id):
    boletas = Boleta.objects.filter(recinto_id=rec_id)
    return render(request, "votos/boleta.html",{"boletas": boletas})

def datosBoleta(request, bol_id):
    datosBoletas = Boleta.objects.filter(id=bol_id)
    return render(request, "votos/datos_boleta.html",{"datosBoletas": datosBoletas})

def api(request):
    boletas = Boleta.objects.all()
    return JsonResponse(list(boletas.values()),safe=False)

def export(request, rec_id):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Nro Mesa','CC Pres','CC Dip','FPV Pres','FPV Dip','MTS Pres','MTS Dip','UCS Pres','UCS Dip',
                     'MAS Pres','MAS Dip','21F Pres','21F Dip','PDC Pres','PDC Dip','MNR Pres','MNR Dip',
                     'PAN Pres','PAN Dip','Blancos Pres','Blancos Dip','Nulos Pres','Nulos Dip'])
    
    for boleta in Boleta.objects.filter(recinto_id=rec_id).values_list('id_mesa','cc_pres','cc_dip','fpv_pres','fpv_dip','mts_pres','mts_dip','ucs_pres','ucs_dip',
                                                                       'mas_pres','mas_dip','f21_pres','f21_dip','pdc_pres','pdc_dip','mnr_pres','mnr_dip',
                                                                       'pan_pres','pan_dip','blancos_pres','blancos_dip','nulos_pres','nulos_dip'):
        writer.writerow(boleta)
        
    response['Content-Disposition'] = 'attachment; filename="boletas.csv"'
    return response

#Reporte Personalizado
def exportDatos(request, bol_id):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    
    #mesa
    writer.writerow(['NUMERO DE MESA'])
    datosBoletas = Boleta.objects.filter(id=bol_id)
    for boleta in datosBoletas.values_list('id_mesa'):
        writer.writerow(boleta)
        
    #titulo
    writer.writerow(['PRESIDENTE','DIPUTADO'])
    
    #cc
    datosBoletas = Boleta.objects.filter(id=bol_id)
    for boleta in datosBoletas.values_list('cc_pres','cc_dip'):
        writer.writerow(['CC'])
        writer.writerow(boleta)       
    #fpv
    datosBoletas = Boleta.objects.filter(id=bol_id)
    for boleta in datosBoletas.values_list('fpv_pres','fpv_dip'):
        writer.writerow(['FPV'])
        writer.writerow(boleta)       
    #mts
    datosBoletas = Boleta.objects.filter(id=bol_id)
    for boleta in datosBoletas.values_list('mts_pres','mts_dip'):
        writer.writerow(['MTS'])
        writer.writerow(boleta)     
    #ucs
    datosBoletas = Boleta.objects.filter(id=bol_id)
    for boleta in datosBoletas.values_list('ucs_pres','ucs_dip'):
        writer.writerow(['UCS'])
        writer.writerow(boleta)
    #mas
    datosBoletas = Boleta.objects.filter(id=bol_id)
    for boleta in datosBoletas.values_list('mas_pres','mas_dip'):
        writer.writerow(['MAS'])
        writer.writerow(boleta)
    #21f
    datosBoletas = Boleta.objects.filter(id=bol_id)
    for boleta in datosBoletas.values_list('f21_pres','f21_dip'):
        writer.writerow(['21F'])
        writer.writerow(boleta)
    #pdc
    datosBoletas = Boleta.objects.filter(id=bol_id)
    for boleta in datosBoletas.values_list('pdc_pres','pdc_dip'):
        writer.writerow(['PDC'])
        writer.writerow(boleta)
    #mnr
    datosBoletas = Boleta.objects.filter(id=bol_id)
    for boleta in datosBoletas.values_list('mnr_pres','mnr_dip'):
        writer.writerow(['MNR'])
        writer.writerow(boleta)
    #pan
    datosBoletas = Boleta.objects.filter(id=bol_id)
    for boleta in datosBoletas.values_list('pan_pres','pan_dip'):
        writer.writerow(['PAN'])
        writer.writerow(boleta)
    #blancos
    datosBoletas = Boleta.objects.filter(id=bol_id)
    for boleta in datosBoletas.values_list('blancos_pres','blancos_dip'):
        writer.writerow(['Blancos'])
        writer.writerow(boleta)
    #nulos
    datosBoletas = Boleta.objects.filter(id=bol_id)
    for boleta in datosBoletas.values_list('nulos_pres','nulos_dip'):
        writer.writerow(['Nulos'])
        writer.writerow(boleta)
   
    response['Content-Disposition'] = 'attachment; filename="boletaDatos.csv"'
    return response