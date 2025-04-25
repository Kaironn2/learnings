from django.contrib import admin
from cars.models import Brand, Car


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ['id', 'name']
    search_fields = ('name',)
    ordering = ('name',)

    def __str__(self):
        return self.name

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'brand', 'factory_year', 'model_year', 'price')
    list_display_links = ['id', 'model', 'brand', 'factory_year', 'model_year', 'price']
    search_fields = ('model', 'brand')
    list_filter = ('factory_year', 'model_year')
    ordering = ('-price',)

    def __str__(self):
        return self.model


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
