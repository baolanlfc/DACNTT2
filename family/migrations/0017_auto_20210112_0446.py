# Generated by Django 2.2.17 on 2021-01-11 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0016_auto_20210112_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Ngày sinh'),
        ),
        migrations.AlterField(
            model_name='member',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo'),
        ),
        migrations.AlterField(
            model_name='member',
            name='family',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family.Family', verbose_name='Tên dòng họ'),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family.MemberGender', verbose_name='Giới tính'),
        ),
        migrations.AlterField(
            model_name='member',
            name='is_root',
            field=models.BooleanField(default=False, verbose_name='Thành viên gốc'),
        ),
        migrations.AlterField(
            model_name='member',
            name='live_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family.MemberLiveStatus', verbose_name='Hiện trạng'),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Hình ảnh'),
        ),
        migrations.AlterField(
            model_name='member',
            name='more_information',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Thông tin thêm'),
        ),
        migrations.AlterField(
            model_name='member',
            name='nickname',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Tên thường gọi'),
        ),
        migrations.AlterField(
            model_name='member',
            name='parent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family.Member', verbose_name='Phụ huynh'),
        ),
        migrations.AlterField(
            model_name='member',
            name='partner_name',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Tên vợ/chồng'),
        ),
        migrations.AlterField(
            model_name='member',
            name='real_name',
            field=models.CharField(max_length=500, verbose_name='Họ tên'),
        ),
        migrations.AlterField(
            model_name='member',
            name='rip_date',
            field=models.DateField(blank=True, null=True, verbose_name='Ngày mất'),
        ),
    ]
