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
                'roll_no' : 1001,
                'name' : 'Abhishek',
                'age' : 34
            },
            {
                'roll_no' : 1032,
                'name' : 'Mayuri',
                'age' : 33
            },
            {
                'roll_no' : 1002,
                'name' : 'Ajay',
                'age' : 34
            },
            {
                'roll_no' : 1069,
                'name' : 'Sreesh',
                'age' : 34
            },
            {
                'roll_no' : 1049,
                'name' : 'Pramod',
                'age' : 33
            }
        ]
        for data in dataset:
            # data validation
            # by roll no
            roll_no = data['roll_no']
            #checking if roll_no exists or not
            existing_record = Student.objects.filter(roll_no=roll_no).exists()
            if not existing_record:
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'Student with roll no {roll_no} already exists'))

        self.stdout.write(self.style.SUCCESS('Data inserted successfully.'))
        