from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper

def allowed_users(group_allowed):
    def docerator(view_func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0]
                if str(group) == group_allowed:
                    allowed = True
                else:
                    allowed = False
                return view_func(request, allowed,*args, **kwargs)
        return wrapper
    return docerator