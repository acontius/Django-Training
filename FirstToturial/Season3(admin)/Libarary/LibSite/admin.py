from django.contrib import admin
from . import models

class BookInline(admin.TabularInline):
    model = models.Book
    extra = 1


class BookInstanceInline(admin.StackedInline):
    model = models.BookInstance
    extra = 1

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    # fields are used to show the input bars and to control them
    # fields = [('name' , 'lastName'),('birthDate' , 'deathDate')]

    # fieldsets are better cause they customise the fields to what you want
    fieldsets = (
        ('Identity', {
            "fields" : ('name' , 'lastName')
        }),
        ('Status' , {
            "fields" : ('birthDate' , 'deathDate')
        }),
    )
    

    # list_diplays are used to display the things that we want to show 
    list_display = ('__str__','birthDate')
    # list_filters are used to search
    list_filter = ('name' , 'deathDate')

    inlines = [BookInline]

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    # fields = [('title' , 'author'),('summary' , 'genere')]
    fieldsets = (
        ("Author's Informations", {
           "fields" :  ('title' , 'author')
        }),
       ("Book's Informations" , {
            "fields" : ('summary' , 'genere')
        }),
    )
    
    list_display = ('title' , 'author' , 'diplay_genere')
    list_filter = ('genere' , 'author')


    inlines = [BookInstanceInline]


@admin.register(models.Genere)
class GenereAdmin(admin.ModelAdmin):
    list_diplay = ('name')


@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display =('status' , 'due_back' , 'id')
    list_filter = ('due_back' , 'status')


    # fields = [('book','status' , 'id') ,'imprint' , 'due_back']
    fieldsets = (
        ('Title' , {
            'fields' : ('book' , 'id')
        }),
        ('status', {
            'fields' : ('imprint' , 'due_back' , 'status') 
        }),
    )