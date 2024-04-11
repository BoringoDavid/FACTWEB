# Generated by Django 5.0.4 on 2024-04-09 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FactWebApp', '0003_aboutimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='designImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='design_images/')),
                ('description', models.TextField()),
            ],
        ),
    ]
