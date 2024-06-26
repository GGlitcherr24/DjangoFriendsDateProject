from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

#Класс для отображения бд людей в админке
class PersonAdmin(admin.ModelAdmin):
    p = User.objects.all()
    list_display = ('id', 'first_name', 'last_name', 'photo', 'hobby', 'is_published')
    list_display_links = ('id', 'first_name', 'last_name')
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    prepopulated_fields = {"slug": ("first_name", "last_name")}

#Класс для отображения бд пола в админке
class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender')
    list_display_links = ('id', 'gender')
    search_fields = ('gender',)
    prepopulated_fields = {"slug": ("gender",)}


admin.site.register(Person, PersonAdmin)
admin.site.register(Gender, GenderAdmin)
