# Generated by Django 2.0 on 2018-12-30 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20181227_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(null=True, verbose_name='Birthdate'),
        ),
    ]