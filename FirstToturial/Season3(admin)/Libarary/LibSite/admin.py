from django.contrib import admin
from . import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('__str__','birthDate')
    list_filter = ('name' , 'deathDate')

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title' , 'author' , 'diplay_genere')


@admin.register(models.Genere)
class GenereAdmin(admin.ModelAdmin):
    list_diplay = ('name')


@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display =('status' , 'due_back' , 'id')