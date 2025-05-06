from django.core.management.base import BaseCommand
from cashflowapp.models import Status, Type, Category, Subcategory

class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating initial data...')
        
        # Create statuses
        self.stdout.write('Creating statuses...')
        statuses = [
            'Business',
            'Personal',
            'Tax',
        ]
        for status_name in statuses:
            Status.objects.get_or_create(name=status_name)
        
        # Create types
        self.stdout.write('Creating types...')
        types = [
            'Income',
            'Expense',
        ]
        
        type_objects = {}
        for type_name in types:
            type_obj, created = Type.objects.get_or_create(name=type_name)
            type_objects[type_name] = type_obj
        
        # Create categories and subcategories
        self.stdout.write('Creating categories and subcategories...')
        categories_data = {
            'Income': [
                ('Salary', ['Main Job', 'Part-time']),
                ('Investment', ['Dividends', 'Interest']),
            ],
            'Expense': [
                ('Infrastructure', ['VPS', 'Proxy']),
                ('Marketing', ['Farpost', 'Avito']),
                ('Utilities', ['Electricity', 'Water', 'Internet']),
                ('Food', ['Groceries', 'Restaurants']),
            ],
        }
        
        for type_name, categories in categories_data.items():
            type_obj = type_objects[type_name]
            for category_name, subcategories in categories:
                category, created = Category.objects.get_or_create(
                    name=category_name,
                    type=type_obj
                )
                
                for subcategory_name in subcategories:
                    Subcategory.objects.get_or_create(
                        name=subcategory_name,
                        category=category
                    )
        
        self.stdout.write(self.style.SUCCESS('Initial data created successfully!'))
