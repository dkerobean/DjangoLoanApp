# Generated by Django 4.2.1 on 2023-09-09 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0013_alter_loanapplication_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='mobile_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
