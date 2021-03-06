# Generated by Django 2.2.17 on 2021-01-10 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0003_family_parentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberGender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MemberLiveStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('live_status', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='family',
            name='intro',
            field=models.TextField(max_length=500),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_name', models.CharField(max_length=500)),
                ('nickname', models.CharField(max_length=500)),
                ('birth_date', models.DateField()),
                ('member_image', models.FileField(blank=True, null=True, upload_to='')),
                ('rip_date', models.DateField()),
                ('more_information', models.TextField(max_length=500)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('family', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family.Family')),
                ('gender', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family.MemberGender')),
                ('live_status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family.MemberLiveStatus')),
                ('parent', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family.Member')),
            ],
        ),
    ]
