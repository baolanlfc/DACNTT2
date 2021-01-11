from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import FamilyForm
from .models import Family,Member
from pprint import pprint
import json

def listFamily(request):
    list_family = Family.objects.all()
    return render(request,"index.html",{"list_family":list_family})

def familyDetail(request,id):
    #article = Article.objects.filter(id = id).first()   
    Data = get_object_or_404(Family,id = id)
    Data.number_of_members = Member.objects.filter(family_id=id).count()
    Data.member_list = Member.objects.filter(family_id=id).order_by('birth_date')
    return render(request,"family_detail.html",{"Data":Data})

def buildUserRoleTree(parentID):
        branch = []
        members = Member.objects.filter(parent_id=parentID).filter(is_root=False)
        for member in members:
            array = {}
            array["text"] = member.real_name
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
            fn_data["text"] = dt.real_name
            fn_data["value"] = dt.id
    item = buildUserRoleTree(root_id)
    fn_data["items"] = item
    return render(request, "tree_family.html", {'Data': fn_data})

def update_tree(request):
    print(123)

    return request