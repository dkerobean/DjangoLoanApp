# Generated by Django 4.2.1 on 2023-09-09 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0012_alter_loanapplication_duration_delete_loanstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='postal_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
