# Generated by Django 4.2.4 on 2023-08-16 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactMe_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactme',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
