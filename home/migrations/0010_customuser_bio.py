# Generated by Django 3.1.7 on 2021-03-17 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_image_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.CharField(default='NULL', max_length=250),
        ),
    ]
