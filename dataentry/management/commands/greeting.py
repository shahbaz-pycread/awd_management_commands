from django.core.management.base import BaseCommand

# Proposed command: py manage.py greeting  UserName
# Proposed Output: Hi {UserName}, Good Morning
class Command(BaseCommand):
    help = 'Greets the user'
    
    def add_arguments(self, parser):
        parser.add_argument('name',type=str,help='Specifies user name')
    
    def handle(self, *args, **kwargs):
        # self.stdout.write('Hi Shahbaz, Good Evening!') # Static
        name = kwargs['name']
        greeting = f'Hello {name}, Good Morning!'
        #self.stdout.write(greeting)
        # With style
        self.stdout.write(self.style.SUCCESS(greeting))
    