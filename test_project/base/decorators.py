from django.http import HttpResponse
from django.shortcuts import redirect
from functools import wraps

def staff_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_staff:
            return func(request, *args, **kwargs)
        return HttpResponse('YOU ARE NOT AUTHORISED HERE!')
    return wrapper