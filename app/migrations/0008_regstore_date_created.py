# Generated by Django 4.0.6 on 2022-07-17 14:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_regstore_alter_xmltodict_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='regstore',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
