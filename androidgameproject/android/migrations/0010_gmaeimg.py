# Generated by Django 3.0 on 2020-08-14 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('android', '0009_auto_20200814_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='gmaeimg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='', upload_to='gamepic/image')),
                ('title', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
