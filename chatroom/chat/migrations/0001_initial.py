# Generated by Django 2.0.1 on 2018-01-22 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
    ]
