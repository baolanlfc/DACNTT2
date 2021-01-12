from django import forms
from .models import Family,Member

class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ["parentage","family_name","address","intro"]

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["real_name","nickname","birth_date","gender","member_image","is_root","parent"]