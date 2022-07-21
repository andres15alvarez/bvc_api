import csv
from datetime import date
from django.apps import apps
from django.core.management.base import BaseCommand, no_translations, CommandError
from apps.exchange.models import ExchangeRate


class Command(BaseCommand):

    help = "Dump in the database the records of the exchange rate USD-VES"

    def add_arguments(self, parser):
        parser.add_argument('--csv', nargs=1, type=str)

    @no_translations
    def handle(self, *args, **options):
        if 'csv' not in options:
            raise CommandError('CSV File is needed!')
        list_exchange_rate = []
        currency = apps.get_model('currency', 'Currency')
        usd_currency, _ = currency.objects.get_or_create(
            code="USD",
            name="United States Dollar"
        )
        ves_currency, _ = currency.objects.get_or_create(
            code="VES",
            name="Bolivar"
        )
        with open(options['csv'][0], newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                date_splitted = row['Date'].split('-')
                list_exchange_rate.append(
                    ExchangeRate(
                        date=date(
                            int(date_splitted[0]),
                            int(date_splitted[1]),
                            int(date_splitted[2])
                        ),
                        open=float(row['Open']),
                        high=float(row['High']),
                        low=float(row['Low']),
                        close=float(row['Price']),
                        from_currency=usd_currency,
                        to_currency=ves_currency
                    )
                )
        objects_created = ExchangeRate.objects.bulk_create(list_exchange_rate)
        self.stdout.write(self.style.SUCCESS(f"{len(objects_created)} rows inserted"))

