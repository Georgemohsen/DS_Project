# Generated by Django 2.0.4 on 2018-05-06 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0, max_length=1),
        ),
    ]
