# Generated by Django 4.2.4 on 2023-08-19 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myskill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillname', models.CharField(max_length=100)),
                ('Degree', models.IntegerField(verbose_name=range(0, 100))),
            ],
        ),
    ]
