from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def index(request):
    t = get_template("index.html")
    html = t.render(Context({}))
    return HttpResponse(html)

def product_list(request):
    t = get_template("list.html")
    html = t.render(Context({"pagelist": ["p2", "p3", "p4"], "pagenum": 4}))
    return HttpResponse(html)
