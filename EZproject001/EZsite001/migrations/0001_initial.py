# Generated by Django 3.0.2 on 2020-02-11 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('p1', models.CharField(max_length=300)),
                ('p2', models.CharField(max_length=300)),
                ('p3', models.CharField(max_length=300)),
                ('p4', models.CharField(max_length=300)),
                ('p5', models.CharField(max_length=300)),
                ('p6', models.CharField(max_length=300)),
                ('p7', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'forum',
            },
        ),
    ]
