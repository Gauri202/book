# Generated by Django 4.1.1 on 2022-09-08 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookcode', models.IntegerField(default=0)),
                ('booktitle', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
            ],
        ),
    ]