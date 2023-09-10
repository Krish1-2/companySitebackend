# Generated by Django 4.1.7 on 2023-09-10 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Electricals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FRPPoleBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50)),
                ('product', models.CharField(max_length=100)),
                ('review', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SwitchGear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=100)),
            ],
        ),
    ]
