# Generated by Django 5.1.4 on 2024-12-10 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FactWebApp', '0016_image_posted_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='magazine_type',
            field=models.TextField(default='Architectural magazine'),
        ),
    ]