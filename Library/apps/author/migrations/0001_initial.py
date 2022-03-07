# Generated by Django 4.0.3 on 2022-03-07 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='authors',
            fields=[
                ('author_id', models.IntegerField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(blank=True, max_length=100)),
                ('lastName', models.CharField(blank=True, max_length=100)),
                ('nationality', models.CharField(blank=True, max_length=2)),
                ('birthDate', models.DateField(blank=True)),
            ],
        ),
    ]
