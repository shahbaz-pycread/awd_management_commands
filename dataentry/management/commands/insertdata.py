from django.core.management.base import BaseCommand
from dataentry.models import Student
class Command(BaseCommand):
    help = 'It will insert data to the database'
    
    def handle(self, *args, **kwargs):
        # logic goes here
        # add 1 data
        # Student.objects.create(roll_no=1033,name='Shahbaz', age=31)
        # add static dataset => list of dictionary
        dataset = [
            {
                'roll_no' : 1033,
                'name' : 'Alam',
                'age' : 31
            },
            {
                'roll_no' : 1018,
                'name' : 'Chirag',
                'age' : 33
            },
            {
                'roll_no' : 1017,
                'name' : 'Chinmay',
                'age' : 33
            },
            {
                'roll_no' : 1053,
                'name' : 'Shashank',
                'age' : 30
            },
            {
                'roll_no' : 1049,
                'name' : 'Pramod',
                'age' : 33
            }
        ]
        for data in dataset:
            Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])

        self.stdout.write(self.style.SUCCESS('Data inserted successfully.'))
        