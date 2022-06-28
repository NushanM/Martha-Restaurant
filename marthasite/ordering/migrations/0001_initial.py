# Generated by Django 4.0.5 on 2022-06-18 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dessert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dessert', models.CharField(max_length=200)),
                ('dessert_price', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MainDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_dish', models.CharField(max_length=200)),
                ('main_dish_price', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_dish', models.CharField(max_length=200)),
                ('wadai', models.BooleanField()),
                ('dhal', models.BooleanField()),
                ('fish', models.BooleanField()),
                ('dessert', models.CharField(max_length=200)),
                ('order_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='SideDishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side_dish', models.CharField(max_length=200)),
                ('side_dish_price', models.CharField(max_length=200)),
            ],
        ),
    ]