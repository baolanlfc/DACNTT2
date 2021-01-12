from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import FamilyForm,MemberForm
from .models import Family,Member
from pprint import pprint
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json

def listFamily(request):
    keyword = request.GET.get("keyword")
    if keyword:
        list_family = Family.objects.filter(id = keyword)
        return render(request,"index.html",{"list_family":list_family})
    list_family = Family.objects.filter(status='Approved').order_by('-id')
    return render(request,"index.html",{"list_family":list_family})


def familyDetail(request,id):
    #article = Article.objects.filter(id = id).first()   
    Data = get_object_or_404(Family,id = id)
    Data.number_of_members = Member.objects.filter(family_id=id).count()
    Data.member_list = Member.objects.filter(family_id=id).order_by('birth_date')
    if request.user == Data.created_user:
        Data.is_update_family = ''
    else: 
        Data.is_update_family = 'none'
    return render(request,"family_detail.html",{"Data":Data})

@login_required(login_url = "user:login")
def addFamily(request):
    form = FamilyForm(request.POST or None)

    if form.is_valid():
        family = form.save(commit=False)
        
        family.created_user_id = request.user.id
        family.save()

        messages.success(request,"Dòng họ được thêm thành công")
        return redirect("family_detail",family.id)
    return render(request,"add_family.html",{"form":form})

@login_required(login_url = "user:login")
def updateFamily(request,id):
    family = get_object_or_404(Family,id = id)
    form = FamilyForm(request.POST or None,request.FILES or None,instance = family)
    if form.is_valid():
        family = form.save(commit=False)
        family.save()

        messages.success(request,"Thông tin dòng họ đã cập nhật thành công")
        return redirect("family_detail",id)
    return render(request,"update_family.html",{"form":form})


@login_required(login_url = "user:login")
def addMember(request, family_id):
    form = MemberForm(request.POST or None)
    if form.is_valid():
        family = form.save(commit=False)

        family.created_user_id = request.user.id
        family.family_id = family_id
        family.save()
        
        messages.success(request,"Thành viên được thêm thành công")
        return redirect("family_detail",family_id)
    return render(request,"add_member.html",{"form":form})

@login_required(login_url = "user:login")
def updateMember(request,member_id):
    family = get_object_or_404(Member,id = member_id)
    form = MemberForm(request.POST or None,request.FILES or None,instance = family)
    if form.is_valid():
        family = form.save(commit=False)
        family.save()

        messages.success(request,"Thông tin thành viên đã cập nhật thành công")
        return redirect("family_detail",family.family_id)
    return render(request,"update_member.html",{"form":form})

def buildUserRoleTree(parentID):
        branch = []
        members = Member.objects.filter(parent_id=parentID).filter(is_root=False)
        for member in members:
            array = {}
            if str(member.birth_date) != 'None':
                birth_date = str(member.birth_date)
            else: 
                birth_date = 'Không rõ'

            if str(member.rip_date) != 'None':
                rip_date = str(member.rip_date)
            else: 
                rip_date = 'Không rõ'

            array["text"] = member.real_name + ' (' + birth_date + ' - ' + rip_date + ')'
            array["value"] = member.id
            if member.id == parentID:
                branch.append(array)
            else: 
                children = buildUserRoleTree(member.id)
                if children:
                    array["items"] = children
                branch.append(array)
        return branch

def show_tree(request,id):
    Data = Member.objects.filter(family_id=id)
    fn_data = {}
    for dt in Data:
        if dt.is_root:
            root_id = dt.id
            if str(dt.birth_date) != 'None':
                birth_date = str(dt.birth_date)
            else: 
                birth_date = 'Không rõ'

            if str(dt.rip_date) != 'None':
                rip_date = str(dt.rip_date)
            else: 
                rip_date = 'Không rõ'
            fn_data["text"] = dt.real_name + ' (' + birth_date + ' - ' + rip_date + ')'
            fn_data["value"] = dt.id
            item = buildUserRoleTree(root_id)
    fn_data["items"] = item
    return render(request, "tree_family.html", {'Data': fn_data})

def update_tree(request):
    print(123)

    return request