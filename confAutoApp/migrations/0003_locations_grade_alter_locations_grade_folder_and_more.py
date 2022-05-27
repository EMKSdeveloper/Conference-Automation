# Generated by Django 4.0.3 on 2022-04-21 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confAutoApp', '0002_locations_which_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='grade',
            field=models.CharField(choices=[('FIVE', '5'), ('SIX', '6'), ('SEVEN', '7'), ('EIGHT', '8'), ('NINE', '9'), ('TEN', '10'), ('ELEVEN', '11'), ('TWELVE', '12')], default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='locations',
            name='grade_folder',
            field=models.TextField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='locations',
            name='original_file',
            field=models.TextField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='locations',
            name='split_files',
            field=models.TextField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='locations',
            name='which_task',
            field=models.CharField(choices=[('SSRC', 'Split and Sort Report Cards'), ('SSSP', 'Split and Sort Supplemental Pages'), ('MOF', 'Move Old Conference Files into a Folder')], default=' ', max_length=200),
        ),
    ]