# Generated by Django 4.1.7 on 2023-03-28 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0002_hero_hero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='hero',
        ),
    ]
