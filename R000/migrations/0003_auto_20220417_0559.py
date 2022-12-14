# Generated by Django 3.2 on 2022-04-17 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('R000', '0002_auto_20220417_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='studant',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='studant',
            name='toll_status',
            field=models.CharField(choices=[('yes', 'تم التسديد '), ('no', 'لم يتم التسديد')], max_length=190, null=True),
        ),
        migrations.AlterField(
            model_name='studant',
            name='accept_type',
            field=models.CharField(choices=[('ganral', 'قبول عم'), ('privet', 'قبول خاص')], max_length=190, null=True),
        ),
        migrations.AlterField(
            model_name='studant',
            name='gender',
            field=models.CharField(choices=[('meal', 'زكر'), ('femeal', 'انثى')], max_length=190, null=True),
        ),
    ]
