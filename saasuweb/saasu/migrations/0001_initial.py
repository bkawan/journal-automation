# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 07:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import saasu.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='csv/', validators=[saasu.validators.FileValidator(allowed_extensions=['csv']), saasu.validators.FileValidator(max_size_=25165824)])),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'csv_files',
            },
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_number', models.IntegerField()),
                ('date', models.DateField()),
                ('summary', models.TextField(blank=True, null=True)),
                ('tags', models.TextField(blank=True, null=True)),
                ('currency', models.TextField(max_length=3)),
                ('amount', models.FloatField()),
                ('debit_credit', models.CharField(max_length=10)),
                ('account_name', models.IntegerField()),
                ('tax_code', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[('Successful', 'Successful'), ('Error', 'Error')], max_length=11)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('csv_input', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saasu.CSVInput')),
            ],
            options={
                'db_table': 'journal_entries',
            },
        ),
    ]