# Generated by Django 3.2.9 on 2021-12-29 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('followers_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='followers',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='followers',
            name='post',
        ),
    ]
