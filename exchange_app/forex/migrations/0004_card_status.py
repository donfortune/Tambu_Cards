# Generated by Django 5.1 on 2024-09-17 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0003_service_remove_card_service_card_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=8),
        ),
    ]
