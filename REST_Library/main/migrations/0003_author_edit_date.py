# Generated by Django 3.1.7 on 2021-07-29 22:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_delete_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='edit_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
