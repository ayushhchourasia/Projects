# Generated by Django 5.0.3 on 2024-05-01 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_stafff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=20)),
                ('last', models.CharField(max_length=10)),
                ('mail', models.CharField(max_length=20)),
                ('mob', models.IntegerField()),
                ('pswdd', models.CharField(max_length=10)),
                ('cpswdd', models.CharField(max_length=10)),
                ('genderr', models.CharField(max_length=7)),
            ],
        ),
    ]
