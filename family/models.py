from django.db import models


# Create your models here.
class Family(models.Model):
    parentage = models.ForeignKey("family.Parentage",on_delete = models.CASCADE,default=1, verbose_name="Họ")
    family_name = models.CharField(max_length = 500, verbose_name="Tên dòng họ")
    address = models.CharField(max_length = 500, verbose_name="Nguyên quán")
    intro = models.TextField(max_length = 500,null = True,blank=True, verbose_name="Giới thiệu về dòng họ")
    PUBLIC_TYPE_CHOICES = [('Public', 'Công khai'), ('Private', 'Riêng tư')]
    public_type = models.CharField(max_length=50,choices=PUBLIC_TYPE_CHOICES,default='Public',)
    password = models.CharField(max_length = 500,default=1)
    STATUS_CHOICES = [('Approved', 'Đã duyệt'), ('Waiting for approving', 'Đợi duyệt')]
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Waiting for approving', verbose_name="Trạng thái")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    created_user = models.ForeignKey("auth.User",on_delete = models.CASCADE,default=1)

    def __str__(self):
        return self.family_name

class Parentage(models.Model):
    parentage = models.CharField(max_length = 500)
    
    def __str__(self):
        return self.parentage

class Member(models.Model):
    real_name = models.CharField(max_length = 500, verbose_name="Họ tên")
    nickname = models.CharField(max_length = 500,null = True,blank=True, verbose_name="Tên thường gọi")
    birth_date = models.DateField(null = True,blank=True, verbose_name="Ngày sinh")
    gender = models.ForeignKey("family.MemberGender",on_delete = models.CASCADE,default=1, verbose_name="Giới tính")
    member_image = models.FileField(blank = True,null = True, verbose_name="Hình ảnh")
    live_status = models.ForeignKey("family.MemberLiveStatus",on_delete = models.CASCADE,default=1, verbose_name="Hiện trạng")
    rip_date = models.DateField(null = True,blank=True, verbose_name="Ngày mất")
    more_information = models.TextField(max_length = 500,null = True,blank=True, verbose_name="Thông tin thêm")
    family = models.ForeignKey("family.Family",on_delete = models.CASCADE,default=1, verbose_name="Tên dòng họ")
    is_root = models.BooleanField(default=False, verbose_name="Thành viên gốc")
    parent = models.ForeignKey("self",on_delete = models.CASCADE,default=1, verbose_name="Phụ huynh")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    partner_name = models.CharField(max_length = 500,null = True,blank=True, verbose_name="Tên vợ/chồng")
    def __str__(self):
        return self.real_name

class MemberGender(models.Model):
    gender = models.CharField(max_length = 50)

    def __str__(self):
        return self.gender
    
class MemberLiveStatus(models.Model):
    live_status = models.CharField(max_length = 50)

    def __str__(self):
        return self.live_status
