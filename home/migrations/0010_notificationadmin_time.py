# Generated by Django 3.2.8 on 2021-10-16 13:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20211016_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationadmin',
            name='time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]