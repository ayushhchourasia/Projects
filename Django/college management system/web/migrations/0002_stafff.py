# Generated by Django 5.0.3 on 2024-05-01 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stafff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ffname', models.CharField(max_length=20)),
                ('llname', models.CharField(max_length=10)),
                ('eemail', models.CharField(max_length=20)),
                ('pphone', models.IntegerField()),
                ('pswrd', models.CharField(max_length=10)),
                ('cpswrd', models.CharField(max_length=10)),
                ('ggender', models.CharField(max_length=7)),
            ],
        ),
    ]
