# Generated by Django 4.2.16 on 2024-10-10 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_alter_account_account_id_alter_account_app_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='app_token',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
