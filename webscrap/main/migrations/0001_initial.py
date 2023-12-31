# Generated by Django 4.2.1 on 2023-06-23 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webname', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weblink', models.CharField(max_length=200)),
                ('webinfo', models.CharField(max_length=1000)),
                ('websource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.webcontent')),
            ],
        ),
    ]
