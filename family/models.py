from django.db import models


# Create your models here.
class Family(models.Model):
    parentage = models.ForeignKey("family.Parentage",on_delete = models.CASCADE,default=1)
    family_name = models.CharField(max_length = 500)
    address = models.CharField(max_length = 500)
    intro = models.TextField(max_length = 500,null = True,blank=True)
    PUBLIC_TYPE_CHOICES = [('Public', 'Công khai'), ('Private', 'Riêng tư')]
    public_type = models.CharField(max_length=50,choices=PUBLIC_TYPE_CHOICES,default='Public',)
    password = models.CharField(max_length = 500,default=1)
    STATUS_CHOICES = [('Approved', 'Đã duyệt'), ('Waiting for approving', 'Đợi duyệt')]
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Waiting for approving',)
    created_date = models.DateTimeField(auto_now_add=True)
    created_user = models.ForeignKey("auth.User",on_delete = models.CASCADE,default=1)

    def __str__(self):
        return self.family_name

class Parentage(models.Model):
    parentage = models.CharField(max_length = 500)
    
    def __str__(self):
        return self.parentage

class Member(models.Model):
    real_name = models.CharField(max_length = 500)
    nickname = models.CharField(max_length = 500,null = True,blank=True)
    birth_date = models.DateField(null = True,blank=True)
    gender = models.ForeignKey("family.MemberGender",on_delete = models.CASCADE,default=1)
    member_image = models.FileField(blank = True,null = True)
    live_status = models.ForeignKey("family.MemberLiveStatus",on_delete = models.CASCADE,default=1)
    rip_date = models.DateField(null = True,blank=True)
    more_information = models.TextField(max_length = 500,null = True,blank=True)
    family = models.ForeignKey("family.Family",on_delete = models.CASCADE,default=1)
    is_root = models.BooleanField(default=False)
    parent = models.ForeignKey("self",on_delete = models.CASCADE,default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    partner_name = models.CharField(max_length = 500,null = True,blank=True)
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
