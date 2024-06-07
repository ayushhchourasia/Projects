# Generated by Django 5.0.3 on 2024-05-01 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_addstaff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addstudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=10)),
                ('last', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('area', models.CharField(max_length=20)),
                ('r1', models.CharField(max_length=7)),
                ('hname', models.CharField(max_length=30)),
                ('per', models.IntegerField()),
                ('hsname', models.CharField(max_length=30)),
                ('percent', models.IntegerField()),
                ('anum', models.IntegerField()),
                ('pnum', models.IntegerField()),
                ('email', models.CharField(max_length=20)),
            ],
        ),
    ]
