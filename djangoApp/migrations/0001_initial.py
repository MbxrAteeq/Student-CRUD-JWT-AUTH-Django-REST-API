# Generated by Django 3.2.5 on 2021-11-08 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('city', models.CharField(max_length=45)),
                ('phoneNumber', models.IntegerField(max_length=13)),
            ],
        ),
    ]
