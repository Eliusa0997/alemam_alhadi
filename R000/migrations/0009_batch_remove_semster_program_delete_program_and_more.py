# Generated by Django 4.0.1 on 2022-11-24 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('R000', '0008_semster_remove_studant_batch_delete_batch_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batch_department', to='R000.department')),
            ],
        ),
        migrations.RemoveField(
            model_name='semster',
            name='program',
        ),
        migrations.DeleteModel(
            name='Program',
        ),
        migrations.AddField(
            model_name='semster',
            name='Batch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semster_batch', to='R000.batch'),
        ),
    ]