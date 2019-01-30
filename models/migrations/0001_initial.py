# Generated by Django 2.1.5 on 2019-01-29 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_number', models.CharField(max_length=255)),
                ('request_date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity_required', models.PositiveIntegerField()),
                ('unit_of_measure', models.CharField(max_length=10)),
                ('estimated_unit_price', models.FloatField()),
                ('total_estimated_price', models.FloatField()),
                ('delivery_location', models.TextField(blank=True, null=True)),
                ('date_required', models.DateField()),
                ('emergency', models.BooleanField(default=False)),
                ('sample_required', models.BooleanField(default=False)),
                ('item', models.CharField(blank=True, max_length=255, null=True)),
                ('quote', models.PositiveIntegerField(blank=True, null=True)),
                ('round', models.PositiveIntegerField(blank=True, null=True)),
                ('exact_match', models.BooleanField(default=False)),
                ('quote_requested_date', models.DateField(blank=True, null=True)),
                ('suppliers', models.CharField(max_length=255)),
                ('quote_received_date', models.DateField(blank=True, null=True)),
                ('quoted_unit_price', models.FloatField(blank=True, null=True)),
                ('total_quote_price', models.FloatField(blank=True, null=True)),
                ('quote_submitted_date', models.DateField(blank=True, null=True)),
                ('quote_selected', models.BooleanField(default=False)),
                ('quote_accepted_date', models.DateField(blank=True, null=True)),
                ('forecast', models.CharField(blank=True, max_length=255, null=True)),
                ('baseline_spend', models.FloatField(blank=True, null=True)),
                ('savings_amount', models.FloatField(blank=True, null=True)),
                ('savings_percent', models.FloatField(blank=True, null=True)),
                ('savings_levels_applied', models.CharField(blank=True, max_length=255, null=True)),
                ('request_to_quote_cycle_time', models.CharField(blank=True, max_length=255, null=True)),
                ('supplier_response_cycle_time', models.CharField(blank=True, max_length=255, null=True)),
                ('quote_acceptance_cycle_time', models.CharField(blank=True, max_length=255, null=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Buyer')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Company')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Currency')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Requester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RequestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Saving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfSavings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='information',
            name='request_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.RequestType'),
        ),
        migrations.AddField(
            model_name='information',
            name='requester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Requester'),
        ),
        migrations.AddField(
            model_name='information',
            name='saving',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Saving'),
        ),
        migrations.AddField(
            model_name='information',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Status'),
        ),
        migrations.AddField(
            model_name='information',
            name='type_of_savings',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.TypeOfSavings'),
        ),
    ]
