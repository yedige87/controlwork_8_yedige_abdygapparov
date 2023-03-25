from django.contrib import admin

from webapp.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'category', 'photo')
    list_filter = ('id', 'name', 'category')
    search_fields = ('name', 'text')
    fields = ('text', 'name', 'category', 'photo')
    readonly_fields = ('id',)


admin.site.register(Product, ProductAdmin)
