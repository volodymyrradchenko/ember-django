# Generated by Django 2.0.7 on 2018-08-31 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('id',)},
        ),
        migrations.RemoveField(
            model_name='post',
            name='created',
        ),
    ]