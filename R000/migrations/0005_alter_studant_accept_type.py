# Generated by Django 3.2 on 2022-04-17 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('R000', '0004_alter_studant_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studant',
            name='accept_type',
            field=models.CharField(choices=[('عام', 'قبول عم'), ('privet', 'قبول خاص')], max_length=190, null=True),
        ),
    ]