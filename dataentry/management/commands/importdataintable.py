from django.core.management.base import BaseCommand, CommandError
#from dataentry.models import Student, Customer
# import all apps
from django.apps import apps
import csv
# Proposed Command: py manage.py importdata file_path model_name

class Command(BaseCommand):
    help = "Import data from CSV file"
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')
        parser.add_argument('model_name', type=str, help='Name of the model')
    
    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]
        model_name = kwargs['model_name'].capitalize()
        print(file_path)
        
        # Search for model across all installed apps
        model = None
        for app_config in apps.get_app_configs():
            # Try to search for the models inside the app
            try:
                model = apps.get_model(app_config.label,model_name)
                break # Stop searching once the model is found
            except LookupError:
                continue # Model not found in the app, continue searching in other apps
        
        if not model:
            raise CommandError(f'Model "{model_name}" not found in any app')
        
        # open the file with read mode
        with open(file_path, 'r') as file:
            # Read the file
            reader = csv.DictReader(file)
            for row in reader:
                # Create the data
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        
