# Generated by Django 4.0.6 on 2022-07-17 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_xmltodict_date_added_alter_storejson_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xmltodict',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
