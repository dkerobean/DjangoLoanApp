# Generated by Django 4.2.1 on 2023-05-27 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_loanapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='mobile_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='postal_code',
            field=models.IntegerField(),
        ),
    ]
