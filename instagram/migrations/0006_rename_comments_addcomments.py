# Generated by Django 3.2.12 on 2022-03-11 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0005_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='AddComments',
        ),
    ]