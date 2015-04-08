from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from uploader import MONGO
from .forms import UploadFileForm
from .processor import handle_uploaded_file

def index(request):
    data = MONGO.search_data({}).limit(6)
    picture_list = []
    for _data in data:
        d = {}
        d['url'] = 'http://7xi4me.com1.z0.glb.clouddn.com/%s' % _data["id"]
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

def login(request):
    if request.method == "GET":
        GET = request.GET
        if "username" not in GET and "password" not in GET:
            t = get_template("login.html")
            html = t.render(Context({}))
            return HttpResponse(html)
        username = GET['username']
        password = GET['password']

        if username == "zhang" and password == "zixuan":
            return HttpResponse("Login Success")

@csrf_exempt
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            content = request.FILES['file'].read()
            handle_uploaded_file(content, request.POST['title'], request.POST['description'])
            return HttpResponse("Upload Success")
        else:
            return HttpResponse("Upload Failed")
    else:
        form = UploadFileForm()
        return render_to_response("upload.html", {"form": form})
