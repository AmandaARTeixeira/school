# Generated by Django 5.0.3 on 2024-10-04 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
                ('level', models.CharField(default='B', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=30)),
                ('cpf', models.CharField(max_length=11)),
                ('birth_date', models.DateField()),
                ('phone', models.CharField(max_length=14)),
            ],
        ),
    ]
