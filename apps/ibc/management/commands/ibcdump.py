import csv
from datetime import date
from django.core.management.base import BaseCommand, no_translations, CommandError
from apps.ibc.models import IBC


class Command(BaseCommand):

    help = "Dump in the database the records of the IBC"

    def add_arguments(self, parser):
        parser.add_argument('--csv', nargs=1, type=str)

    @no_translations
    def handle(self, *args, **options):
        if 'csv' not in options:
            raise CommandError('CSV File is needed!')
        with open(options['csv'][0], newline='') as f:
            reader = csv.DictReader(f)
            list_ibc = []
            for row in reader:
                date_splitted = row['Date'].split('/')
                list_ibc.append(
                    IBC(
                        date=date(int(date_splitted[2]), int(date_splitted[0]), int(date_splitted[1])),
                        ibc=row['IBC']
                    )
                )
        objects_created = IBC.objects.bulk_create(list_ibc)
        self.stdout.write(self.style.SUCCESS(f"{len(objects_created)} rows inserted"))

