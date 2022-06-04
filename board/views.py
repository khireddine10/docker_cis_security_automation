from django.shortcuts import render, redirect, HttpResponse
from django.http import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .docerators import unauthenticated_user, allowed_users
from .models import host
from .utils import hosts as h

# Create your views here.


@unauthenticated_user
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("home")
        else:
            messages.error(
                request, "User not found, you don't have one! ask your admin")
    return render(request, "login.html", {})


@login_required(login_url="signin")
def logout(request):
    auth_logout(request)
    return redirect("signin")


@login_required(login_url="signin")
def home(request):
    last_id = host.objects.all()[:1].get().id
    return render(request, "dashboard.html", locals())


@login_required(login_url="signin")
@allowed_users("correcteur")
def hosts(request, allowed, pk):
    last_id = host.objects.all()[:1].get().id
    hosts = host.objects.all()
    myhost = host.objects.get(id=pk)
    connected = h.test_connectivity(
        str(myhost.hostname), str(myhost.password), str(myhost.user))
    allowed = allowed
    return render(request, "hosts.html", locals())


@login_required(login_url="signin")
@allowed_users("correcteur")
def addHost(request, allowed):
    if allowed:
        if request.method == "POST":
            hostname = request.POST.get("hostname")
            ip = request.POST.get("ip")
            hostuser = request.POST.get("hostuser")
            password = request.POST.get("password")
            description = request.POST.get("description")
            last_id = host.objects.all()[:1].get().id
            newHost = host(hostname=hostname, ip=ip, user=hostuser,
                           password=password, description=description)
            newHost.save()
            messages.success(request, "host created successfully")
            return redirect("hosts/" + str(last_id))
        else:
            return HttpResponse(status=405)
    else:
        return HttpResponse(status=405)


@login_required(login_url="signin")
@allowed_users("correcteur")
def modifyHost(request, allowed):
    if allowed:
        if request.method == "POST":
            hostid = request.POST.get("mhost")
            obj = host.objects.get(pk=hostid)
            obj.hostname = request.POST.get("hostname")
            obj.ip = request.POST.get("ip")
            obj.user = request.POST.get("hostuser")
            obj.password = request.POST.get("password")
            obj.description = request.POST.get("description")
            obj.save()
            last_id = host.objects.all()[:1].get().id
            return redirect("hosts/" + str(last_id))
        else:
            return HttpResponse(status=405)
    else:
        return HttpResponse(status=405)
    pass


@login_required(login_url="signin")
@allowed_users("correcteur")
def deleteHost(request, allowed):
    if allowed:
        if request.method == "POST":
            hostid = request.POST.get("mhost")
            obj = host.objects.get(id=hostid)
            obj.delete()
            last_id = host.objects.all()[:1].get().id
            return redirect("hosts/" + str(last_id))
        else:
            return HttpResponse(status=405)
    else:
        return HttpResponse(status=405)
    pass


@login_required(login_url="signin")
def cisChecks(request):
    last_id = host.objects.all()[:1].get().id
    return render(request, "cischecks.html", locals())


@login_required(login_url="signin")
def vulChecks(request):
    last_id = host.objects.all()[:1].get().id
    return render(request, "hosts.html", locals())
