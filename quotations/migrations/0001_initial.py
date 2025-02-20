# Generated by Django 4.2.4 on 2024-10-23 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=15)),
                ('quotation_number', models.IntegerField()),
                ('car_type', models.CharField(choices=[('new', 'New'), ('used', 'Used')], max_length=10)),
                ('cpr', models.CharField(max_length=11)),
                ('date', models.DateField()),
                ('to', models.CharField(choices=[('NBB', 'NBB'), ('BBK', 'BBK'), ('AUB', 'AUB'), ('BCFC', 'BCFC'), ('NFH', 'NFH'), ('BISB', 'BISB')], max_length=10)),
                ('car_brand', models.CharField(max_length=50)),
                ('chassis_no', models.CharField(max_length=50)),
                ('engine_no', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=30)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('downpayment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
