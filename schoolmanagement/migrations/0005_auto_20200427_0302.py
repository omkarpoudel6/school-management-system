# Generated by Django 3.0 on 2020-04-27 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmanagement', '0004_auto_20200427_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolmanagement.Student_info'),
        ),
    ]