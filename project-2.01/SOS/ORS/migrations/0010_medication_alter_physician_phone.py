# Generated by Django 5.1.4 on 2025-01-30 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORS', '0009_physician'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=30)),
                ('illness', models.CharField(max_length=50)),
                ('prescriptionDate', models.DateField(max_length=20)),
                ('dosage', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'sos_Medication',
            },
        ),
        migrations.AlterField(
            model_name='physician',
            name='phone',
            field=models.CharField(default='', max_length=13),
        ),
    ]
