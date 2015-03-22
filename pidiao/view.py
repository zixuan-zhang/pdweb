from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

from uploader import MONGO

def index(request):
    data = MONGO.search_data({}).limit(6)
    picture_list = []
    for _data in data:
        d = {}
        d['url'] = 'http://7xi4me.com1.z0.glb.clouddn.com/%s' % _data["id"]
        print d['url']
        d['name'] = _data["id"]
        d['des'] = _data['des']
        picture_list.append(d)

    t = get_template("index.html")
    html = t.render(Context({"picture_list": picture_list}))
    return HttpResponse(html)

def product_list(request):
    data = MONGO.search_data({}).limit(6)
    picture_list = []
    for _data in data:
        d = {}
        d['url'] = 'http://7xi4me.com1.z0.glb.clouddn.com/%s' % _data["id"]
        print d['url']
        d['name'] = _data["id"]
        d['des'] = _data['des']
        picture_list.append(d)
    t = get_template("list.html")
    html = t.render(Context({"pagelist": ["p2", "p3", "p4"], "pagenum": 4, "picture_list": picture_list}))
    return HttpResponse(html)
