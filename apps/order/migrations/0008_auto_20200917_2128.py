# Generated by Django 3.0.9 on 2020-09-17 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20200917_2112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='state',
            new_name='place',
        ),
    ]
