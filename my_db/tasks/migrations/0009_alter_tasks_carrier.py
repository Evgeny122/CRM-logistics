# Generated by Django 4.1.5 on 2023-03-06 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list_trans', '0003_alter_carrier_name_editcarrier'),
        ('tasks', '0008_tasks_carrier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='carrier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='list_trans.editcarrier'),
        ),
    ]