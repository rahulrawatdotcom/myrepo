# Generated by Django 3.0 on 2020-07-30 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('android', '0004_auto_20200730_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
