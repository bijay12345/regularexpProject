# Generated by Django 4.0.6 on 2022-07-17 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_regstore_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='regstore',
            name='title',
            field=models.CharField(default='N/A', max_length=200),
            preserve_default=False,
        ),
    ]
