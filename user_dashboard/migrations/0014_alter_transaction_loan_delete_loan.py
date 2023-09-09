# Generated by Django 4.2.1 on 2023-06-02 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_loanapplication_interest_rate_and_more'),
        ('user_dashboard', '0013_alter_transaction_options_loan_verified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='loan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='frontend.loanapplication'),
        ),
        migrations.DeleteModel(
            name='Loan',
        ),
    ]
