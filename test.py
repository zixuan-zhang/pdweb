from pidiao import uploader

qiniu = uploader.Qiniu()
mongo = uploader.Mongo("test")

for i in range(1,7):
    _file = "%d.jpg" % i
    qiniu.upload_file(str(i), _file)
    data = {"id": str(i), "des": "%d%d" % (i, i)}
    mongo.insert_data(data)
