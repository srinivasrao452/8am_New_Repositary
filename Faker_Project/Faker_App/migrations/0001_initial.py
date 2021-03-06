# Generated by Django 3.0.5 on 2021-09-24 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
