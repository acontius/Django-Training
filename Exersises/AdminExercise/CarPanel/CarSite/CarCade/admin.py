from django.contrib import admin
from . import models

class TypeInline(admin.TabularInline):
    model = models.Type
    extra=1


@admin.register(models.Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    fields       = [('name','brand'),'location']
    list_filter  = ('brand','name')
    list_display = ('name','brand','location')
    inlines = [TypeInline]


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Common informations' , {
         'fields' : (('carName','carId') ,'manufacture' ,'carType' , 'fuel')  
        }), 
        ('Usefull informations' , {
            'fields' : [('date','capacity','distance','inventory')]
        })
    )

    list_display = ['carName','manufacture','carType','fuel']
    list_filter = ['carType','fuel','inventory','manufacture','carType']


@admin.register(models.Type)
class TypeAdmin(admin.ModelAdmin):
    fields = ['type']


@admin.register(models.Fuel)
class FuelAdmin(admin.ModelAdmin):
    fields = ['fuel']