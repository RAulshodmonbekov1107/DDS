from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('cashflow/add/', views.CashFlowCreateView.as_view(), name='cashflow_add'),
    path('cashflow/<int:pk>/edit/', views.CashFlowUpdateView.as_view(), name='cashflow_edit'),
    path('cashflow/<int:pk>/delete/', views.CashFlowDeleteView.as_view(), name='cashflow_delete'),
    
    path('dictionary/', views.DictionaryView.as_view(), name='dictionary'),
    
    path('status/add/', views.StatusCreateView.as_view(), name='status_add'),
    path('status/<int:pk>/edit/', views.StatusUpdateView.as_view(), name='status_edit'),
    path('status/<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status_delete'),
    
    path('type/add/', views.TypeCreateView.as_view(), name='type_add'),
    path('type/<int:pk>/edit/', views.TypeUpdateView.as_view(), name='type_edit'),
    path('type/<int:pk>/delete/', views.TypeDeleteView.as_view(), name='type_delete'),
    
    path('category/add/', views.CategoryCreateView.as_view(), name='category_add'),
    path('category/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    
    path('subcategory/add/', views.SubcategoryCreateView.as_view(), name='subcategory_add'),
    path('subcategory/<int:pk>/edit/', views.SubcategoryUpdateView.as_view(), name='subcategory_edit'),
    path('subcategory/<int:pk>/delete/', views.SubcategoryDeleteView.as_view(), name='subcategory_delete'),
    
    path('ajax/get-categories/', views.get_categories, name='ajax_get_categories'),
    path('ajax/get-subcategories/', views.get_subcategories, name='ajax_get_subcategories'),
]
