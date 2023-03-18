# Generated by Django 4.1.5 on 2023-03-08 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_tasks_logist'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('Новая', 'Новая'), ('Грузоперевозка', 'Грузоперевозка'), ('Выгружена', 'Выгружена')], default='Новая', max_length=30),
        ),
    ]
