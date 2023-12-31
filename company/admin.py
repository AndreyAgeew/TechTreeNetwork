from django.contrib import admin
from .models import Company, Product


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'supplier', 'debt', 'created_at')
    list_filter = ('city',)
    search_fields = ('name', 'city')
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)

    clear_debt.short_description = 'Очистить задолженность'

    class Meta:
        model = Company


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'release_date', 'company']
    list_filter = ['company']
    search_fields = ['name', 'model']
