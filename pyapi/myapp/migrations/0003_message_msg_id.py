# Generated by Django 3.2.9 on 2021-11-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20211103_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='msg_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]