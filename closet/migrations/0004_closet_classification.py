# Generated by Django 4.2 on 2023-05-18 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closet', '0003_remove_closet_classification'),
    ]

    operations = [
        migrations.AddField(
            model_name='closet',
            name='classification',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
