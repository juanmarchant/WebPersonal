# Generated by Django 3.2.9 on 2021-11-24 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20211124_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
