# Generated by Django 4.2 on 2023-05-11 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='image',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='post',
        ),
        migrations.AddField(
            model_name='photo',
            name='imagedata',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
