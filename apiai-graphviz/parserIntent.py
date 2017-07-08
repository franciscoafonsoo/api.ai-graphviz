# -*- coding: utf-8 -*-
import os
import json
from pathlib import Path

'''
Class Load:

    Classe responsavel por carregar a pasta intent
    nota:   json.load   - loads a file
            json.loads  - loads a string
'''


class Load:

    def __init__(self):
        self.data = dict()
        self.relativepath = Path('./aquamote/intents')

    def check_path(self, path):
        return True if path.startswith(os.path.abspath(self.relativepath) + '/') else False

    def load_intents(self, path):
        # if self.check_path(path):
        for i, filename in enumerate(os.listdir(path)):
            with open('./aquamote/intents/' + filename, encoding="utf-8") as data_file:
                self.data[filename] = json.load(data_file)
