# Generated by Django 4.1 on 2022-08-11 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('points', models.FloatField()),
                ('quizResolved', models.IntegerField()),
                ('questionsResolved', models.IntegerField()),
                ('registrationDate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
