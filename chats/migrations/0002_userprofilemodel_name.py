# Generated by Django 4.2.6 on 2023-10-23 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilemodel',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
