# Generated by Django 5.1 on 2024-08-25 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertemplate',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]