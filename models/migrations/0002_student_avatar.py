# Generated by Django 5.0.6 on 2024-07-09 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='students'),
        ),
    ]
