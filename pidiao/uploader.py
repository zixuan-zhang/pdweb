"""
Created on 3.17 2015

@Author: Zhang Zixuan(zixuan.zhang.victor@gmail.com)

This script provide API to upload files

"""

from qiniu import Auth
from qiniu.services.storage.uploader import put_data, put_file

import pymongo

class Qiniu:
    
    def __init__(self, bucket_name="pd-picture"):
        self.ACCESS_KEY = "UNipA1LL6APPZ5w_LAOzWXGIWiTpGldohraxjVrs"
        self.SECRET_KEY = "6JMBHzW-BN5C2omz2rFDuj9dCDQy3_9F4ty-DY-d"
        self.BUCKET_NAME = bucket_name
        self.AUTH = None

        self._get_authentation()

    def _get_authentation(self):
        self.AUTH  = Auth(self.ACCESS_KEY, self.SECRET_KEY)

    def upload_data(self, key, data):
        token = self.AUTH.upload_token(self.BUCKET_NAME)
        ret, info = put_data(token, key, data)
        return ret, info

    def upload_file(self, key, file_path, mime_type=None):
        token = self.AUTH.upload_token(self.BUCKET_NAME)
        ret, info = put_file(token, key, file_path, check_crc=True)
        return ret, info

class Mongo:

    def __init__(self, db, ip = "127.0.0.0", port = 11277):
        con = pymongo.Connection()
        self.db = con[db]

    def insert_data(self, data):
        self.db.picture.insert(data)

    def search_data(self, condition=None):
        return self.db.picture.find(condition)

    def find_account(self, condition=None):
        print condition
        result = self.db.account.find_one(condition)
        print result
        return result

MONGO = Mongo("test")
QINIU = Qiniu()
