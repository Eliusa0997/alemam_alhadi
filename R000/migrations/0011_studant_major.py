# Generated by Django 4.0.1 on 2023-01-06 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('R000', '0010_rename_batch_semster_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='studant',
            name='major',
            field=models.CharField(blank=True, max_length=190, null=True),
        ),
    ]
