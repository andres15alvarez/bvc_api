import csv
from datetime import date
from django.apps import apps
from django.core.management.base import BaseCommand, no_translations, CommandError
from apps.stock.models import Stock


class Command(BaseCommand):

    help = "Dump in the database the records of the stocks"

    def add_arguments(self, parser):
        parser.add_argument('--csv', nargs=1, type=str)
        parser.add_argument('--code', nargs=1, type=str)

    @no_translations
    def handle(self, *args, **options):
        if 'csv' not in options:
            raise CommandError('CSV File is needed!')
        if 'code' not in options:
            raise CommandError('Code of the stock is needed!')
        with open(options['csv'][0], newline='') as f:
            reader = csv.DictReader(f)
            list_stock = []
            company = apps.get_model('company', "Company")
            company_stock = company.objects.get_or_create(
                code=options["code"]
            )
            for row in reader:
                date_splitted = row['Date'].split('/')
                list_stock.append(
                    Stock(
                        code=company_stock,
                        date=date(int(date_splitted[2]), int(date_splitted[0]), int(date_splitted[1])),
                        volume= int(float(row['Volumen'])),
                        open=float(row['Apertura Usd/Bs']),
                        high=float(row['Alto Usd/Bs']),
                        low=float(row['Bajo Usd/Bs']),
                        close=float(row['Cierre Usd/Bs']),
                    )
                )
        objects_created = Stock.objects.bulk_create(list_stock)
        self.stdout.write(self.style.SUCCESS(f"{len(objects_created)} rows inserted"))

