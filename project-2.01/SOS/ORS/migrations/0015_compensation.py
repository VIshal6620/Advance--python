# Generated by Django 5.1.4 on 2025-02-11 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORS', '0014_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compensation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffMember', models.CharField(max_length=30)),
                ('paymentAmount', models.CharField(max_length=20)),
                ('dateApplied', models.DateField(max_length=15)),
                ('state', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'sos_Compensation',
            },
        ),
    ]
