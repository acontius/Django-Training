from django.contrib import admin
from . import models

class TypeInlinne(admin.TabularInline):
    model = models.Type
    extra=1

@admin.register(models.Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    fields       = [('name','brand'),'location']
    list_filter  = ('brand','name')
    list_display = ('name','brand','location')
    inlines = [TypeInlinne]

@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Common informations' , {
         'fields' : ('carName' ,'manufacture' ,'carType' ,'carId')   
        }), 
        ('Usefull informations' , {
            'fields' : ('date','capacity','distance','inventory')
        })
    )


@admin.register(models.Type)
class TypeAdmin(admin.ModelAdmin):
    fields = ['type']