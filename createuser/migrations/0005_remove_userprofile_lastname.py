# Generated by Django 3.2.4 on 2021-06-22 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('createuser', '0004_assigntaskfiles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='lastname',
        ),
    ]
