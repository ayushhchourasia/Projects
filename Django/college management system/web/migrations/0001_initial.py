# Generated by Django 5.0.3 on 2024-05-01 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('pswd', models.CharField(max_length=10)),
                ('cpswd', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=7)),
            ],
        ),
    ]
