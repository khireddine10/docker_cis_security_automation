from django.shortcuts import render, redirect, HttpResponse
from django.http import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .docerators import unauthenticated_user, allowed_users
from .models import host, check, correction
from .utils import hosts as h
from .utils import check as c
from .utils import logs
from .utils import corr
from .utils import vuln
from .utils import vulnerability

# Create your views here. 126.8


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
    try:
        last_id = host.objects.all()[:1].get().id
    except:
        last_id = 1
    return render(request, "dashboard.html", locals())


@login_required(login_url="signin")
@allowed_users("correcteur")
def hosts(request, allowed, pk):
    try:
        last_id = host.objects.all()[:1].get().id
    except:
        last_id = 1
    hosts = host.objects.all()
    try:
        myhost = host.objects.get(id=pk)
        connected = h.test_connectivity(
            str(myhost.hostname), str(myhost.password), str(myhost.user))
    except:
        myhost = "nohost"

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
            try:
                last_id = host.objects.all()[:1].get().id
            except:
                last_id = 1
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
            try:
                last_id = host.objects.all()[:1].get().id
            except:
                last_id = 1
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
            try:
                last_id = host.objects.all()[:1].get().id
            except:
                last_id = 1
            return redirect("hosts/" + str(last_id))
        else:
            return HttpResponse(status=405)
    else:
        return HttpResponse(status=405)
    pass


@login_required(login_url="signin")
def cisChecks(request,  pk):
    try:
        last_id = host.objects.all()[:1].get().id
    except:
        last_id = 1
    myrange = range(1, 8)
    hosts = host.objects.all()
    mychecks = check.objects.filter(checknumber=pk)
    try:
        myhost = h.get_hosts_from_invenotry()[0]
    except:
        myhost = None
    return render(request, "cischecks.html", locals())


@login_required(login_url="signin")
@allowed_users("correcteur")
def runCheck(request, allowed):
    if allowed:
        if request.method == "POST":
            checks = request.POST.getlist('checks')
            checks1 = request.POST.getlist('checks1')
            c.delete_inventory()
            for myhostId in checks1:
                myhost = host.objects.get(pk=int(myhostId))
                if h.test_connectivity(str(myhost.hostname), str(myhost.password), str(myhost.user)):
                    c.build_inventory(
                        myhost.hostname, myhost.password, myhost.user)
                else:
                    pass
            c.remove_log_files()
            user = request.POST.get("user")
            password = request.POST.get("password")
            for mycheck in checks:
                c.runcheck(mycheck, user, password)
            try:
                last_id = host.objects.all()[:1].get().id
            except:
                last_id = 1
            myhost = myhosts = h.get_hosts_from_invenotry()[0]
            return redirect("lastcheck/"+myhost)
        else:
            return HttpResponse(status=405)
    else:
        return HttpResponse(status=405)
    pass


@login_required(login_url="signin")
def lastCheck(request, pk):
    list_of_logs = logs.get_host_logs(str(pk))
    my_checks_db = logs.read_log(list_of_logs)
    list_of_hosts = h.get_hosts_from_invenotry()
    myhost = h.get_hosts_from_invenotry()[0]
    try:
        get_check = my_checks_db[pk]
    except:
        get_check = None
    checkNum = str(pk)
    try:
        last_id = host.objects.all()[:1].get().id
    except:
        last_id = 1
    return render(request, "lastcheck.html", locals())


@login_required(login_url="signin")
@allowed_users("correcteur")
def addCor(request, allowed):
    if allowed:
        if request.method == "POST":
            correction.objects.all().delete()
            checks = request.POST.getlist('checks')
            checklist = ""
            for check in checks:
                checklist = checklist + str(check) + "*"
            checklist = checklist[:-1]
            hostname = request.POST.get('checknum')
            newCor = correction(hostname=hostname, checklist=checklist)
            newCor.save()
            corr.remove_corr_log_file(hostname)
            try:
                last_id = host.objects.all()[:1].get().id
            except:
                last_id = 1
            myhost = myhosts = h.get_hosts_from_invenotry()[0]
            return redirect("checkcor/"+myhost)
        else:
            return HttpResponse(status=405)
    else:
        return HttpResponse(status=405)

    try:
        last_id = host.objects.all()[:1].get().id
    except:
        last_id = 1
    return render(request, "checkcor.html", locals())


@login_required(login_url="signin")
@allowed_users("correcteur")
def checkCor(request, allowed, pk):
    myhosts = h.get_hosts_from_invenotry()
    myhost = h.get_hosts_from_invenotry()[0]
    host_get_corr = str(pk)
    try:
        my_correction_results = logs.get_host_corr_logs(host_get_corr)
    except:
        my_correction_results = None
    try:
        my_corr_list = list()
        mycorrection_checklist = correction.objects.get(
            hostname=pk).checklist.split("*")
    except:
        mycorrection = None
    try:
        last_id = host.objects.all()[:1].get().id
    except:
        last_id = 1
    return render(request, "checkcor.html", locals())


@login_required(login_url="signin")
@allowed_users("correcteur")
def runCor(request, allowed):
    if allowed:
        if request.method == "POST":
            checks = request.POST.getlist('checks')
            hostname = request.POST.get('host_get_corr')
            corr.remove_corr_log_file(hostname)
            corr.delete_inventory()
            k = host.objects.get(hostname=hostname)
            corr.build_inventory(str(k.hostname), str(k.password), str(k.user))
            for c in checks:
                corr.run_corr(c, "securityA123*")
            myhost = h.get_hosts_from_invenotry()[0]

        return redirect("checkcor/"+myhost)


@login_required(login_url="signin")
@allowed_users("correcteur")
def vulChecks(request, allowed):

    hosts = host.objects.all()
    try:
        myhost = h.get_hosts_from_invenotry()[0]
    except:
        myhost = myhost = None

    try:
        last_id = host.objects.all()[:1].get().id
    except:
        last_id = 1
    return render(request, "vuln.html", locals())


@login_required(login_url="signin")
@allowed_users("correcteur")
def vulChecksResult(request, allowed, pk):

    hosts = vuln.get_hosts()
    versions = vuln.get_version_logs("127.0.0.1")
    docker_version = versions[0]
    runc_version = versions[1]
    containerd_version = versions[2]
    try:
        myhost = h.get_hosts_from_invenotry()[0]
    except:
        myhost = myhost = None

    try:
        last_id = host.objects.all()[:1].get().id
    except:
        last_id = 1
    return render(request, "results.html", locals())


@login_required(login_url="signin")
@allowed_users("correcteur")
def execute_vuln(request, allowed):
    if allowed:
        if request.method == "POST":
            checks1 = request.POST.getlist('checks1')
            print(checks1)
            vuln.delete_inventory()
            for myhostId in checks1:
                myhost = host.objects.get(pk=int(myhostId))
                if h.test_connectivity(str(myhost.hostname), str(myhost.password), str(myhost.user)):
                    vuln.build_inventory(
                        myhost.hostname, myhost.password, myhost.user)
                else:
                    pass
            vuln.remove_version_files()
            user = request.POST.get("user")
            password = request.POST.get("password")
            vuln.create_versions(password)
            try:
                last_id = host.objects.all()[:1].get().id
            except:
                last_id = 1
            myhost = myhosts = h.get_hosts_from_invenotry()[0]
            return redirect("vulchecks")
        else:
            return HttpResponse(status=405)
    else:
        return HttpResponse(status=405)
    pass
