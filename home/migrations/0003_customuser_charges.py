# Generated by Django 3.1.7 on 2021-03-11 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_customuser_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='charges',
            field=models.CharField(default=0, max_length=4),
        ),
    ]
