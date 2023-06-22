# Generated by Django 4.2.1 on 2023-06-13 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_alter_loanapplication_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], max_length=20)),
                ('loan_application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to='frontend.loanapplication')),
            ],
        ),
    ]
