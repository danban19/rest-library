# Generated by Django 3.1.7 on 2021-07-31 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_author_edit_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('edit_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
