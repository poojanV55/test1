# Generated by Django 3.2.13 on 2022-06-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intern_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intern',
            name='i_description',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Job Description'),
        ),
    ]
