# Generated by Django 4.0.1 on 2022-11-19 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('R000', '0006_auto_20220417_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='studant',
            name='blood_type',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O-', 'O-'), ('O+', 'O+'), ('AB', 'AB')], max_length=190, null=True),
        ),
    ]