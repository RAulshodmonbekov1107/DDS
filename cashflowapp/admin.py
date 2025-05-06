from django.contrib import admin
from .models import Status, Type, Category, Subcategory, CashFlow
# Register your models here.
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)
    search_fields = ('name',)

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category__type', 'category')
    search_fields = ('name',)

@admin.register(CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    list_display = ('date', 'status', 'type', 'category', 'subcategory', 'amount')
    list_filter = ('date', 'status', 'type', 'category', 'subcategory')
    search_fields = ('comment',)
    date_hierarchy = 'date'

