# Generated by Django 2.0.4 on 2018-05-01 19:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
