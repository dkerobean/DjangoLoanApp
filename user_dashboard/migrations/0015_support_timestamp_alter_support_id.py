# Generated by Django 4.2.1 on 2023-06-03 14:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0014_alter_transaction_loan_delete_loan'),
    ]

    operations = [
        migrations.AddField(
            model_name='support',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='support',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
