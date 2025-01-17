# Generated by Django 5.0.3 on 2024-04-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=20)),
                ('patient_relative_name', models.CharField(max_length=20)),
                ('patient_mobile_number', models.IntegerField()),
                ('patient_email', models.EmailField(max_length=254)),
                ('patient_city', models.CharField(max_length=50)),
                ('health_issue', models.CharField(max_length=30)),
                ('appointment_date', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Unmarried', 'Unmarried')], max_length=10)),
            ],
        ),
    ]
