# Generated by Django 3.2.6 on 2021-09-02 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_myapp_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myapp',
            name='image',
            field=models.ImageField(upload_to='my_apps'),
        ),
    ]
