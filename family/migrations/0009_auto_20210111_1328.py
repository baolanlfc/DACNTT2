# Generated by Django 2.2.17 on 2021-01-11 06:28

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0008_member_partner_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_image',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/media'), upload_to=''),
        ),
    ]
