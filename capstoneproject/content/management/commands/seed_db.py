import csv
from django.core.management.base import BaseCommand
from content.models import Seed

class Command(BaseCommand):
    help = "Import the records from the data.csv file to the primary model"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)
    
    def handle(self, *args, **options):
        csv_file = options['csv_file']
        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    seed, created = Seed.objects.get_or_create(
                        name=row['name'],
                        genus=row['genus'],
                        species=row['species'],
                        seed_type='HYBRID',
                        continent=row['continent']
                    )
                    if created:
                        print("It was a success!")
                    else:
                        print("Oops... Something went wrong")
                self.stdout.write(self.style.SUCCESS("Import was succesful!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR("An error ocurred: {e}"))