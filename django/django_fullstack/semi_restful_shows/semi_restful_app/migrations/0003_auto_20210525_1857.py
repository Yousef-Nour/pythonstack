# Generated by Django 3.2.3 on 2021-05-25 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_app', '0002_series_action'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='action',
        ),
        migrations.AlterField(
            model_name='series',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]