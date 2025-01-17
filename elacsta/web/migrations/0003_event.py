# Generated by Django 5.0.6 on 2024-06-28 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000000)),
                ('price', models.CharField(max_length=100)),
                ('pic', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
