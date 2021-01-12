"""home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('home/', include('home.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from family import views as familyView
from article import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',familyView.listFamily,name = "index"),
    path('family/detail/<int:id>',familyView.familyDetail,name = "family_detail"),
    path('family/add_family/',familyView.addFamily,name = "add_family"),
    path('family/update/<int:id>',familyView.updateFamily,name = "update_family"),
    path('family/<int:family_id>/add_member/',familyView.addMember,name = "add_member"),
    path('family/member/<int:member_id>/update/',familyView.updateMember,name = "update_member"),
    path('about/',views.about,name = "about"),
    path('articles/',include("article.urls")),
    path('user/',include("user.urls")),
    path('tree_family/<int:id>', familyView.show_tree,name = "tree_family"),
    path('update_tree', familyView.update_tree,name = 'tree_family.update')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
