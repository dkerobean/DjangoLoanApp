# Generated by Django 4.2.1 on 2023-06-05 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0015_support_timestamp_alter_support_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_content', models.CharField(max_length=250)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('support', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='user_dashboard.support')),
            ],
        ),
    ]
