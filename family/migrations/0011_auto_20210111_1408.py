# Generated by Django 2.2.17 on 2021-01-11 07:08

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0010_auto_20210111_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='parent',
            field=mptt.fields.TreeForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='family.Member'),
        ),
    ]