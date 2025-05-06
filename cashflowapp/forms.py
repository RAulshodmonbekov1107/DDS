from django import forms
from .models import CashFlow, Status, Type, Category, Subcategory

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']

class CashFlowForm(forms.ModelForm):
    class Meta:
        model = CashFlow
        fields = ['date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.none()
        self.fields['subcategory'].queryset = Subcategory.objects.none()
        
        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = Category.objects.filter(type_id=type_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['category'].queryset = self.instance.type.categories.all()
            
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategories.all()
