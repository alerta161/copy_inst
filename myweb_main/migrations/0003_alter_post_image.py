# Generated by Django 3.2.9 on 2021-12-10 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb_main', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
