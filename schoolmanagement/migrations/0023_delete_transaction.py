# Generated by Django 3.0 on 2020-05-01 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmanagement', '0022_remove_transaction_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]