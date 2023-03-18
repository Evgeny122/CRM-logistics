# Generated by Django 4.1.5 on 2023-03-06 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_remove_tasks_carrier'),
        ('list_trans', '0003_alter_carrier_name_editcarrier'),
    ]

    operations = [
        migrations.AddField(
            model_name='editcarrier',
            name='tasks',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.tasks'),
        ),
        migrations.AlterField(
            model_name='editcarrier',
            name='carrier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='list_trans.carrier'),
        ),
    ]