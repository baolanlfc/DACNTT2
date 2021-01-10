from django.contrib import admin
from .models import Family, Member

# Register your models here.

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ['parentage','family_name', 'address', 'intro', 'created_date']
    list_filter = ['created_date']
    search_fields = ['family_name']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['real_name', 'birth_date', 'gender', 'live_status', 'created_date']
    list_filter = ['created_date']
    search_fields = ['real_name']


