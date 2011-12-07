from urllib import unquote
import datetime
import json

from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic.simple import direct_to_template as render
import redis

r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB,
                password=settings.REDIS_PASSWORD)


header_whitelist = (
    'CONTENT_LENGTH',
    'CONTENT_TYPE',
    'REMOTE_ADDR',
    'REMOTE_HOST',
)


def headerkey(id, index):
    return '{}:{}:headers'.format(id, index)


def bodykey(id, index):
    return '{}:{}:body'.format(id, index)


def timestampkey(id, index):
    return '{}:{}:timestamp'.format(id, index)


def create(request):
    id = r.incr('nextbin')
    r.set(id, 0)
    return redirect('view', id=id)


def view(request, id):
    index = r.get(id)

    if request.method == 'GET':
        if index is None:
            return redirect('create')
        ctx = {}
        ctx['id'] = id
        ctx['posts'] = []
        for i in range(0, int(index)):
            ctx['posts'].append({
                'timestamp': r.get(timestampkey(id, i)),
                'headers': r.hgetall(headerkey(id, i)),
                'body': r.hgetall(bodykey(id, i)),
            })
        return render(request, 'view.html', ctx)

    elif request.method == 'POST':
        if index is None:
            return HttpResponseBadRequest()
        index = r.incr(id) - 1
        r.set(timestampkey(id, index), datetime.datetime.now())
        for h, v in request.META.iteritems():
            if h in header_whitelist or h.startswith('HTTP_'):
                r.hset(headerkey(id, index), h, unquote(v))
        for p, v in request.POST.iteritems():
            try:
                d = json.loads(v)
                r.hset(bodykey(id, index), p, json.dumps(d, indent=4))
            except ValueError:
                r.hset(bodykey(id, index), p, v)
        return HttpResponse()

    else:
        return HttpResponseBadRequest()
