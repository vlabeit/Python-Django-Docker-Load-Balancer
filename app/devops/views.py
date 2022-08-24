from django.shortcuts import render
import socket
import sys

def index(request):
    try:
        ip = socket.gethostbyname(socket.gethostname())+":"+sys.argv[-1][-2:]
    except TypeError:
        return HttpResponseForbidden("Something is wrong")
    return render(request, 'devops/index.html', {'ip': ip})

