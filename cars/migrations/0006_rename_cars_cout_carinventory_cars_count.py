# Generated by Django 5.0.6 on 2024-07-02 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_carinventory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carinventory',
            old_name='cars_cout',
            new_name='cars_count',
        ),
    ]
