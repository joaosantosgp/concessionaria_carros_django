from django.contrib import admin
from cars.models import Car, Brand, CarInventory


class BrandsAdmin(admin.ModelAdmin):

    list_display = ('name',)
    search_fields = ('name',)


class CarAdmin(admin.ModelAdmin):

    list_display = ('model', 'brand', 'factoryYear', 'modelYear', 'value')
    search_fields = ('model', 'brand')


admin.site.register(Brand, BrandsAdmin)
admin.site.register(Car, CarAdmin)