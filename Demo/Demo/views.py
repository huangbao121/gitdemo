from django.http import HttpResponse


def index(request):
    return HttpResponse('hello world')


def love(request):
    return HttpResponse('宝宝是猪')


def test(request, num):
    return HttpResponse('test页面%s' % (num))
