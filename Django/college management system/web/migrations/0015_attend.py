# Generated by Django 5.0.3 on 2024-05-04 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_replystudent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attend', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('day', models.CharField(max_length=10)),
                ('p', models.CharField(max_length=10)),
            ],
        ),
    ]
