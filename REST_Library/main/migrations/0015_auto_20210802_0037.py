# Generated by Django 3.1.7 on 2021-08-02 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210801_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='edit_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='edit_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
