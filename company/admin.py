from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from .models import Company, Product


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'view_supplier_link', 'debt', 'created_at')
    list_filter = ('city',)
    search_fields = ('name', 'city')
    actions = ['clear_debt']

    def view_supplier_link(self, obj):
        if obj.supplier:
            url = reverse("admin:company_company_change", args=[obj.supplier.pk])
            return format_html('<a href="{}">{}</a>', url, obj.supplier.name)
        return '-'

    view_supplier_link.short_description = 'Поставщик'

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)

    clear_debt.short_description = 'Очистить задолженность'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'company')
    list_filter = ('company',)
    search_fields = ('name', 'model')
