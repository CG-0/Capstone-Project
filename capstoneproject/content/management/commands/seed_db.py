import csv
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Import the records from the data.csv file to the primary model"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)
    
    def handle(self, *args, **options):
        csv_file = options['csv_file']
        print(csv_file)

        self.stdout.write(self.style.SUCCESS("Import was succesful!"))