# Generated by Django 4.1.4 on 2023-01-19 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adminregdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(blank=True, max_length=50, null=True)),
                ('EMAIL', models.CharField(blank=True, max_length=50, null=True)),
                ('MOBILE', models.IntegerField(blank=True, null=True)),
                ('USERNAME', models.CharField(blank=True, max_length=50, null=True)),
                ('PASSWORD', models.CharField(blank=True, max_length=50, null=True)),
                ('IMAGE', models.ImageField(upload_to='profile')),
            ],
        ),
    ]
