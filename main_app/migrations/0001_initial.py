# Generated by Django 3.0.5 on 2020-05-02 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('MessageID', models.BigIntegerField(primary_key=True, serialize=False)),
                ('UserIDFrom', models.CharField(max_length=25)),
                ('UserIDTo', models.DateTimeField()),
                ('ProductID', models.BigIntegerField()),
                ('MessageBody', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('ProductID', models.BigIntegerField(primary_key=True, serialize=False)),
                ('UserID', models.BigIntegerField()),
                ('ProductName', models.CharField(max_length=250)),
                ('Price', models.PositiveSmallIntegerField()),
                ('Pictures', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('username', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
