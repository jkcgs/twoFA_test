from base64 import b32encode, b32decode
from datetime import datetime

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pyotp


def index(_):
    return render(_, 'main.html')


@csrf_exempt
def encode(request):
    if 'content' not in request.POST:
        return HttpResponseBadRequest('missing content parameter')

    cont = request.POST['content'].encode('utf-8')
    return HttpResponse(b32encode(cont))


@csrf_exempt
def decode(req):
    if 'content' not in req.POST:
        return HttpResponseBadRequest('missing content parameter')

    cont = req.POST['content'].encode('utf-8')
    return HttpResponse(b32decode(cont))


@csrf_exempt
def getotp(req):
    if 'secret' not in req.POST:
        return HttpResponseBadRequest('missing secret parameter')

    totp = pyotp.TOTP(req.POST['secret'])
    return HttpResponse(totp.now())


@csrf_exempt
def geturl(req):
    if 'secret' not in req.POST:
        return HttpResponseBadRequest('missing secret parameter')

    totp = pyotp.TOTP(req.POST['secret'])
    return HttpResponse(totp.provisioning_uri('djtest'))


@csrf_exempt
def verify(req):
    if 'secret' not in req.POST or 'code' not in req.POST:
        return HttpResponseBadRequest('missing secret or code parameters')

    now = datetime.now()
    totp = pyotp.TOTP(req.POST['secret'])
    offsets = 2
    codes = [totp.now()]
    for i in range(offsets):
        codes.append(totp.at(now.timestamp() + 30*(i+1)))
        codes.append(totp.at(now.timestamp() - 30*(i+1)))

    return HttpResponse(req.POST['code'] in codes)
