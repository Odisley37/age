# Generated by Django 5.1.3 on 2024-11-30 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outflows', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='outflow',
            options={},
        ),
        migrations.RenameField(
            model_name='outflow',
            old_name='Product',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='outflow',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]