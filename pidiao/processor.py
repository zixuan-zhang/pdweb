import time
import hashlib

from django.http import HttpRequest, HttpResponseRedirect

from .uploader import MONGO
from .uploader import QINIU

def handle_uploaded_file(content, title, description):
    QINIU.upload_data(title, content)
    data = {"id": title, "des": description}
    MONGO.insert_data(data)

def check_login(func):
    """
    check if user is login
    """

    def _check_login(*args, **kwargs):
        print "in check login"
        fname = func.func_name
        if len(args) >= 1 and isinstance(args[0], HttpRequest):
            request = args[0]
            pwmd5 = request.session.get("pwmd5", None)
            timestamp = request.session.get("timestamp", None)
            if pwmd5 and pwmd5 == hashlib.md5("doublezhang".encode('utf-8')).hexdigest() and timestamp and (int(time.time()) - int(timestamp) < 20 * 60):
                return func(*args, **kwargs)
            else:
                return HttpResponseRedirect("/login", {"error": "please login"})
    return _check_login
