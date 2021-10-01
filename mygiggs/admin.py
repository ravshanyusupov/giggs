from django.contrib import admin
from .models import Car, Sort
# Register your models here.


class slug(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    # list_filter = ('name',)
    # list_editable = ('name',)

class sort(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('type',)}


admin.site.register(Car, slug)
admin.site.register(Sort, sort)
