# Generated by Django 2.2.7 on 2019-11-28 11:36

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('police_hotline', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=13), blank=True, null=True, size=3)),
                ('hospital_hotline', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=13), blank=True, null=True, size=3)),
            ],
        ),
    ]