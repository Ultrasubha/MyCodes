import csv
from django.core.management.base import BaseCommand
from iplApp.models import IPLMatch, IPLDelivery
from django.db import transaction


class Command(BaseCommand):
    help = 'Load data from CSV files into Django models'

    def handle(self):
        with transaction.atomic():
            # Load IPL Matches data
            with open('iplApp/management/commands/DataFiles/matches.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    IPLMatch.objects.create(**row)

            # Load IPL Deliveries data
            with open('iplApp/management/commands/DataFiles/deliveries.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    match_id = row.pop('match_id')
                    match = IPLMatch.objects.get(id=match_id)
                    IPLDelivery.objects.create(match=match, **row)

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
