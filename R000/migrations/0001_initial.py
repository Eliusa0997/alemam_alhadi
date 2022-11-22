# Generated by Django 3.2 on 2022-04-16 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_college', to='R000.college')),
            ],
        ),
        migrations.CreateModel(
            name='Studant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studant_batch', to='R000.batch')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program_department', to='R000.department')),
            ],
        ),
        migrations.AddField(
            model_name='batch',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batch_program', to='R000.program'),
        ),
    ]
