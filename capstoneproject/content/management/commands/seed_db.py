import csv
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Import the records from the data.csv file to the primary model"