# Generated by Django 4.2.4 on 2023-10-18 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Password', models.CharField(max_length=10)),
            ],
        ),
    ]
