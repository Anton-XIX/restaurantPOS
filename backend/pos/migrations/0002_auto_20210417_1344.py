# Generated by Django 3.1.7 on 2021-04-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos_label', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='is_ready',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]
