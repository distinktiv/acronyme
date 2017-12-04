import os

from flask import json


class Utils(object):
    def __init__(self):
        pass


    def get_file_content(self, file_path):
        acros = open(file_path, "r")
        if os.stat(file_path).st_size == 0:
            content = []
        else:
            content = json.loads(acros.read())
        acros.close()
        return content
