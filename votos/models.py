from django.db import models

# Create your models here.

class Departamento(models.Model):
    nombre_dep = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'departamento'
        verbose_name_plural = 'departamentos'
    def __str__(self):
        return self.nombre_dep


class Provincia(models.Model):
    nombre_prov = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'provincia'
        verbose_name_plural = 'provincias'
    def __str__(self):
        return self.nombre_prov


class Municipio(models.Model):
    nombre_mun = models.CharField(max_length=50)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'municipio'
        verbose_name_plural = 'municipios'
    def __str__(self):
        return self.nombre_mun


class Localidad(models.Model):
    nombre_loc = models.CharField(max_length=50)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'localidad'
        verbose_name_plural = 'localidades'
    def __str__(self):
        return self.nombre_loc


class Recinto(models.Model):
    nombre_rec = models.CharField(max_length=100)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'recinto'
        verbose_name_plural = 'recintos'
    def __str__(self):
        return self.nombre_rec
     
        
class Boleta(models.Model):
    id_mesa = models.CharField(max_length=20)
    
    cc_pres = models.IntegerField(blank=True, null=True)
    cc_dip = models.IntegerField(blank=True, null=True)
    fpv_pres = models.IntegerField(blank=True, null=True)
    fpv_dip = models.IntegerField(blank=True, null=True)
    mts_pres = models.IntegerField(blank=True, null=True)
    mts_dip = models.IntegerField(blank=True, null=True)
    ucs_pres = models.IntegerField(blank=True, null=True)
    ucs_dip = models.IntegerField(blank=True, null=True)
    mas_pres = models.IntegerField(blank=True, null=True)
    mas_dip = models.IntegerField(blank=True, null=True)
    f21_pres = models.IntegerField(blank=True, null=True)
    f21_dip = models.IntegerField(blank=True, null=True)
    pdc_pres = models.IntegerField(blank=True, null=True)
    pdc_dip = models.IntegerField(blank=True, null=True)
    mnr_pres = models.IntegerField(blank=True, null=True)
    mnr_dip = models.IntegerField(blank=True, null=True)
    pan_pres = models.IntegerField(blank=True, null=True)
    pan_dip = models.IntegerField(blank=True, null=True)
    blancos_pres = models.IntegerField(blank=True, null=True)
    blancos_dip = models.IntegerField(blank=True, null=True)
    nulos_pres = models.IntegerField(blank=True, null=True)
    nulos_dip = models.IntegerField(blank=True, null=True)
    
    recinto = models.ForeignKey(Recinto, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'boleta'
        verbose_name_plural = 'boletas'
    def __str__(self):
        return self.id_mesa


class Jurado(models.Model):
    nombre_jurado = models.CharField(max_length=50)
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'jurado'
        verbose_name_plural = 'jurados'
    def __str__(self):
        return self.nombre_jurado