# Generated by Django 4.1.7 on 2023-03-28 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0003_remove_hero_hero'),
    ]

    operations = [
        migrations.AddField(
            model_name='ability',
            name='ability',
            field=models.ManyToManyField(to='heroes.hero'),
        ),
    ]
