# Generated by Django 5.0.7 on 2024-08-02 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourist',
            name='spotimage',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
