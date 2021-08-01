# Generated by Django 3.1.7 on 2021-08-01 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210801_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authors',
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='main.book'),
            preserve_default=False,
        ),
    ]