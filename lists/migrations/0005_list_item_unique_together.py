# Generated by Django 3.0.4 on 2020-03-23 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20200316_0912'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('list', 'text')},
        ),
    ]
