# Generated by Django 5.2.2 on 2025-07-22 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='sentiment',
            field=models.CharField(max_length=20),
        ),
    ]
