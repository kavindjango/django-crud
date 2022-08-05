# Generated by Django 3.2.6 on 2022-08-04 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=90)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'datas',
            },
        ),
    ]
