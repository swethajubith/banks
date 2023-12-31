# Generated by Django 4.2.5 on 2023-11-01 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('ph', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'femlae')], max_length=20)),
                ('address', models.TextField()),
                ('actype', models.CharField(max_length=50, null=True)),
                ('material', models.CharField(max_length=50, null=True)),
                ('state', models.TextField(max_length=10, null=True)),
                ('district', models.TextField(max_length=10, null=True)),
                ('branch', models.TextField(max_length=10, null=True)),
            ],
        ),
    ]
