# Generated by Django 5.1 on 2024-09-18 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0005_offers_alter_card_exchange_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image_url', models.URLField()),
                ('expiry_date', models.DateTimeField()),
                ('claim_url', models.URLField()),
            ],
        ),
    ]
