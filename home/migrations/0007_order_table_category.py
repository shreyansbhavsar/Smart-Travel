# Generated by Django 3.1.7 on 2021-03-16 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_order_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_table',
            name='category',
            field=models.CharField(default='NULL', max_length=12),
        ),
    ]
