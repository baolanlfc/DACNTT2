# Generated by Django 2.2.17 on 2021-01-10 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0002_parentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='parentage',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family.Parentage'),
        ),
    ]
