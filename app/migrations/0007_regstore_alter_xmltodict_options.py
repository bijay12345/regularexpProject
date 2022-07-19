# Generated by Django 4.0.6 on 2022-07-17 14:01

from django.db import migrations, models
import regex_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_xmltodict_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression', regex_field.fields.RegexField(max_length=120)),
            ],
        ),
        migrations.AlterModelOptions(
            name='xmltodict',
            options={'ordering': ('-date_added',)},
        ),
    ]