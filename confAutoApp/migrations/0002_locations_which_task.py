# Generated by Django 4.0.3 on 2022-04-13 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confAutoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='which_task',
            field=models.CharField(default='', max_length=200),
        ),
    ]