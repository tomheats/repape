# Generated by Django 2.2.7 on 2019-11-23 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('write', '0002_remove_write_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='write',
            old_name='likes_total',
            new_name='upvotes_total',
        ),
    ]
