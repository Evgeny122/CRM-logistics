# Generated by Django 4.1.5 on 2023-02-17 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_userinformation_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='bio',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]