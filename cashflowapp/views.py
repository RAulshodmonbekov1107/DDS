from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import CashFlow, Status, Type, Category, Subcategory
from .forms import CashFlowForm, StatusForm, TypeForm, CategoryForm, SubcategoryForm
from .filters import CashFlowFilter

# Create your views here.

class HomeView(ListView):
    model = CashFlow
    template_name = 'cashflow/home.html'
    context_object_name = 'cashflows'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CashFlowFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context

class CashFlowCreateView(CreateView):
    model = CashFlow
    form_class = CashFlowForm
    template_name = 'cashflow/cashflow_form.html'
    success_url = reverse_lazy('home')

class CashFlowUpdateView(UpdateView):
    model = CashFlow
    form_class = CashFlowForm
    template_name = 'cashflow/cashflow_form.html'
    success_url = reverse_lazy('home')

class CashFlowDeleteView(DeleteView):
    model = CashFlow
    template_name = 'cashflow/cashflow_confirm_delete.html'
    success_url = reverse_lazy('home')

class DictionaryView(TemplateView):
    template_name = 'cashflow/dictionary.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'statuses': Status.objects.all(),
            'types': Type.objects.all(),
            'categories': Category.objects.all(),
            'subcategories': Subcategory.objects.all(),
            'status_form': StatusForm(),
            'type_form': TypeForm(),
            'category_form': CategoryForm(),
            'subcategory_form': SubcategoryForm(),
        })
        return context

# Dictionary CRUD views
class StatusCreateView(CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'cashflow/status_form.html'
    success_url = reverse_lazy('dictionary')

class StatusUpdateView(UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'cashflow/status_form.html'
    success_url = reverse_lazy('dictionary')

class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'cashflow/status_confirm_delete.html'
    success_url = reverse_lazy('dictionary')

class TypeCreateView(CreateView):
    model = Type
    form_class = TypeForm
    template_name = 'cashflow/type_form.html'
    success_url = reverse_lazy('dictionary')

class TypeUpdateView(UpdateView):
    model = Type
    form_class = TypeForm
    template_name = 'cashflow/type_form.html'
    success_url = reverse_lazy('dictionary')

class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'cashflow/type_confirm_delete.html'
    success_url = reverse_lazy('dictionary')

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'cashflow/category_form.html'
    success_url = reverse_lazy('dictionary')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'cashflow/category_form.html'
    success_url = reverse_lazy('dictionary')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'cashflow/category_confirm_delete.html'
    success_url = reverse_lazy('dictionary')

class SubcategoryCreateView(CreateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'cashflow/subcategory_form.html'
    success_url = reverse_lazy('dictionary')

class SubcategoryUpdateView(UpdateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'cashflow/subcategory_form.html'
    success_url = reverse_lazy('dictionary')

class SubcategoryDeleteView(DeleteView):
    model = Subcategory
    template_name = 'cashflow/subcategory_confirm_delete.html'
    success_url = reverse_lazy('dictionary')

# AJAX views for dependent dropdowns
def get_categories(request):
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(type_id=type_id).values('id', 'name')
    return JsonResponse(list(categories), safe=False)

def get_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)
