# Generated by Django 5.0.4 on 2024-04-09 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FactWebApp', '0002_rename_image_homeimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_images/')),
                ('description', models.TextField()),
            ],
        ),
    ]