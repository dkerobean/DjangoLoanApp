# Generated by Django 4.2.1 on 2023-05-30 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0011_remove_transaction_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]