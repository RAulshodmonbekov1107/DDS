import django_filters
from django import forms
from .models import CashFlow, Status, Type, Category, Subcategory

class CashFlowFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter(field_name='date', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = django_filters.DateFilter(field_name='date', lookup_expr='lte', widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = CashFlow
        fields = {
            'status': ['exact'],
            'type': ['exact'],
            'category': ['exact'],
            'subcategory': ['exact'],
        }
