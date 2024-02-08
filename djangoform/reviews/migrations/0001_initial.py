# Generated by Django 4.2.7 on 2023-11-22 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('feedback', models.TextField()),
                ('ratings', models.IntegerField()),
                ('favoutite_color', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]