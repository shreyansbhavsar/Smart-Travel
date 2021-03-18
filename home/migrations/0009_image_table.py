# Generated by Django 3.1.7 on 2021-03-17 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_customuser_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=10000)),
                ('description', models.CharField(max_length=200)),
                ('img', models.ImageField(default='NULL', upload_to='pics')),
            ],
        ),
    ]