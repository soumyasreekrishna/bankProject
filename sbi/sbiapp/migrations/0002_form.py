# Generated by Django 4.1.7 on 2023-03-13 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbiapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=250)),
                ('phone', models.BigIntegerField()),
                ('mailid', models.TextField()),
                ('address', models.TextField()),
                ('district', models.CharField(max_length=250)),
                ('account', models.CharField(max_length=250)),
                ('meterial', models.TextField()),
            ],
        ),
    ]
