# Generated by Django 4.2.6 on 2023-10-25 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_userprofilemodel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofilemodel',
            name='name',
        ),
    ]
