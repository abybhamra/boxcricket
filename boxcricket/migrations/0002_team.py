# Generated by Django 2.2.7 on 2019-11-23 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxcricket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('captain', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
