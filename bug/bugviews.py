from django.shortcuts import render
from bug.models import Bug
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
# Create your views here.

#bug 管理
def bug_manage(request):
    username = request.session.get('user', '')
    bug_list = Bug.objects.all()
    return render(request, "bug_manage.html", {"user": username,"bugs": bug_list})



# 搜索功能
@login_required
def bugsearch(request):
    username = request.session.get('user', '') # 读取浏览器登录 Session
    search_bugname = request.GET.get("bugname", "")
    bug_list = Bug.objects.filter(bugname__icontains=search_bugname)
    return render(request,'bug_manage.html', {"user": username,"bugs":bug_list})