# Generated by Django 4.1.7 on 2023-03-28 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0008_ability_abilities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='about_me',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
