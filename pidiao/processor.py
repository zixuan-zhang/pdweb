from .uploader import MONGO
from .uploader import QINIU

def handle_uploaded_file(content, title, description):
    QINIU.upload_data(title, content)
    data = {"id": title, "des": description}
    MONGO.insert_data(data)

