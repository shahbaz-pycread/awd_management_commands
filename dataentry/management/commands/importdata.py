from django.core.management.base import BaseCommand
from dataentry.models import Student
import csv
# Proposed Command: py manage.py importdata file_path

class Command(BaseCommand):
    help = "Import data from CSV file"
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')
    
    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]
        print(file_path)
        # open the file with read mode
        with open(file_path, 'r') as file:
            # Read the file
            reader = csv.DictReader(file)
            for row in reader:
                # Create the data
                Student.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        
