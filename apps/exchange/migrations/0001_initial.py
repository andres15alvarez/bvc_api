# Generated by Django 3.2.14 on 2022-07-20 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open', models.DecimalField(decimal_places=2, max_digits=12)),
                ('close', models.DecimalField(decimal_places=2, max_digits=12)),
                ('high', models.DecimalField(decimal_places=2, max_digits=12)),
                ('low', models.DecimalField(decimal_places=2, max_digits=12)),
                ('date', models.DateField()),
                ('from_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_rates', to='currency.currency')),
                ('to_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_rates', to='currency.currency')),
            ],
            options={
                'verbose_name': 'exchange_rate',
                'verbose_name_plural': 'exchange_rates',
                'db_table': 'exchange_rate',
            },
        ),
    ]