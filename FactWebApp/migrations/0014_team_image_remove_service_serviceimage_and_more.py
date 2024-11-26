# Generated by Django 5.1.3 on 2024-11-26 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FactWebApp', '0013_video_alter_service_serviceimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='team_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/images')),
                ('names', models.TextField()),
                ('position', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='service',
            name='serviceimage',
        ),
        migrations.RemoveField(
            model_name='service',
            name='title',
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='services/'),
        ),
        migrations.AddField(
            model_name='service',
            name='service_title',
            field=models.CharField(default='Default Service Title', max_length=150),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(default='Default service description.'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]