# Generated by Django 4.0.5 on 2022-07-12 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_alter_producto_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='categoria',
            new_name='marca',
        ),
    ]