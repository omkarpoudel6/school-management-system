# Generated by Django 3.0 on 2020-04-26 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(unique=True)),
                ('firstname', models.CharField(max_length=20)),
                ('middlename', models.CharField(blank=True, max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('grade', models.IntegerField()),
                ('fathername', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]