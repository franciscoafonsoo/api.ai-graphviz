# -*- coding: utf-8 -*-
import os

__path__ = [os.path.dirname(os.path.abspath(__file__))]

import json
from pathlib import Path
from . import intent

'''
Class Load:

    Classe responsavel por carregar a pasta intent
    nota:   json.load   - loads a file
            json.loads  - loads a string
'''


class Load:
    def __init__(self):
        self.data = dict()
        self.intents = list()
        self.relativepath = Path('./aquamote/intents')

    def check_path(self, path):
        return True if path.startswith(os.path.abspath(self.relativepath) + '/') else False

    def load_intents(self, path):
        # if self.check_path(path):
        for i, filename in enumerate(os.listdir(path)):
            with open('./aquamote/intents/' + filename, encoding="utf-8") as data_file:
                self.data[filename] = json.load(data_file)

        for key, value in self.data.items():
            self.intents.append(
                intent.Intent(value['name'],
                              value['contexts'],
                              value['responses'],
                              value['events'],
                              value['responses']))
