# Generated by Django 4.2.1 on 2023-05-30 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0009_alter_loan_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='reference',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
