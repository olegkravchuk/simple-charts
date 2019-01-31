# Generated by Django 2.1.5 on 2019-01-31 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buyer',
            options={'ordering': ['name'], 'verbose_name': 'Buyer', 'verbose_name_plural': 'Buyers'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name'], 'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name': 'Currency', 'verbose_name_plural': 'Currencies'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['name'], 'verbose_name': 'Department', 'verbose_name_plural': 'Departments'},
        ),
        migrations.AlterModelOptions(
            name='information',
            options={'verbose_name': 'Information', 'verbose_name_plural': 'Informations'},
        ),
        migrations.AlterModelOptions(
            name='requester',
            options={'ordering': ['name'], 'verbose_name': 'Requester', 'verbose_name_plural': 'Requesters'},
        ),
        migrations.AlterModelOptions(
            name='requesttype',
            options={'ordering': ['name'], 'verbose_name': 'Request type', 'verbose_name_plural': 'Request types'},
        ),
        migrations.AlterModelOptions(
            name='saving',
            options={'ordering': ['name'], 'verbose_name': 'Saving', 'verbose_name_plural': 'Savings'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ['name'], 'verbose_name': 'Status', 'verbose_name_plural': 'Statuses'},
        ),
        migrations.AlterModelOptions(
            name='typeofsavings',
            options={'ordering': ['name'], 'verbose_name': 'Type of saving', 'verbose_name_plural': 'Type of savings'},
        ),
    ]
