# Generated by Django 5.1.3 on 2024-12-17 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FactWebApp', '0017_image_magazine_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]